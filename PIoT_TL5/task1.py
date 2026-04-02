import bluetooth
import sqlite3
import time
from sense_hat import SenseHat

def init_db():
    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (
        mac TEXT PRIMARY KEY,
        name TEXT,
        last_seen TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def check_device(mac, name):
    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM devices WHERE mac=?", (mac,))
    result = cursor.fetchone()
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if result:
        cursor.execute("UPDATE devices SET last_seen=? WHERE mac=?", (current_time, mac))
        conn.commit()
        conn.close()
        return "known"
    else:
        cursor.execute("INSERT INTO devices (mac, name, last_seen) VALUES (?, ?, ?)",
                       (mac, name, current_time))
        conn.commit()
        conn.close()
        return "new"

def scan_devices():
    sense = SenseHat()
    
    while True:
        print("\nScanning...")
        nearby_devices = bluetooth.discover_devices(duration=5, lookup_names=True)
        
        for mac, name in nearby_devices:
            if not name:
                name = "Unknown"

            status = check_device(mac, name)

            print(f"{name} ({mac}) detected")

            if status == "known":
                message = f"Hello {name}"
            else:
                message = f"Welcome {name}"

            print(message)
            sense.show_message(message, scroll_speed=0.05)

        time.sleep(5)

init_db()
scan_devices()