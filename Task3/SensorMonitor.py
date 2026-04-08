import json
import sqlite3
import time
from sense_hat import SenseHat


class SensorMonitor:
    def __init__(self):
        self.sense = SenseHat()
        self.paused = False

        self.load_config()
        self.setup_db()

        self.last_read_time = -10
        self.display_index = 0
        self.last_display_time = 0

    def load_config(self):
        try:
            with open("enviro_config.json") as f:
                self.config = json.load(f)

            for key in ["temperature", "humidity", "pressure", "orientation"]:
                if key not in self.config:
                    raise ValueError(f"Missing config: {key}")

        except Exception as e:
            print("Config error:", e)
            exit()

    def setup_db(self):
        self.conn = sqlite3.connect("envirotrack.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL,
            pressure REAL,
            pitch REAL,
            roll REAL,
            yaw REAL,
            temp_status TEXT,
            humidity_status TEXT,
            pressure_status TEXT,
            orientation_status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def classify(self, value, min_val, max_val):
        if value < min_val:
            return "Low"
        elif value > max_val:
            return "High"
        else:
            return "Comfortable"

    def classify_orientation(self, pitch, roll, yaw):
        o = self.config["orientation"]

        if abs(pitch) > o["pitch_limit"] or abs(roll) > o["roll_limit"]:
            return "Tilted"
        return "Aligned"

    def read_sensors(self):
        temp = self.sense.get_temperature() - 2
        humidity = self.sense.get_humidity()
        pressure = self.sense.get_pressure()

        o = self.sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]

        return temp, humidity, pressure, pitch, roll, yaw

    def log_data(self, data):
        print("Saving data...", data) 

        self.cursor.execute("""
        INSERT INTO readings 
        (temperature, humidity, pressure, pitch, roll, yaw,
         temp_status, humidity_status, pressure_status, orientation_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)

        self.conn.commit()

    def display(self, temp, hum, pres, pitch, roll, yaw, statuses):
        colors = {
            "Low": [0, 0, 255],
            "High": [255, 0, 0],
            "Comfortable": [0, 255, 0],
            "Tilted": [255, 165, 0],
            "Aligned": [0, 255, 0]
        }

        now = time.time()

        if now - self.last_display_time > 5:
            self.display_index = (self.display_index + 1) % 3
            self.last_display_time = now

        if self.display_index == 0:
            self.sense.show_message(f"T:{int(temp)}", text_colour=colors[statuses[0]])
        elif self.display_index == 1:
            self.sense.show_message(f"H:{int(hum)}", text_colour=colors[statuses[1]])
        else:
            self.sense.show_message(f"P:{int(pitch)} R:{int(roll)}", text_colour=colors[statuses[3]])

    def handle_input(self):
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                self.paused = not self.paused

    def run(self):
        
        temp = hum = pres = pitch = roll = yaw = 0
        temp_status = hum_status = pres_status = orient_status = "Comfortable"

        while True:
            self.handle_input()

            if self.paused:
                time.sleep(0.1)
                continue

            now = time.time()

            if now - self.last_read_time > 10:
                temp, hum, pres, pitch, roll, yaw = self.read_sensors()

                temp_status = self.classify(
                    temp, self.config["temperature"]["min"], self.config["temperature"]["max"]
                )
                hum_status = self.classify(
                    hum, self.config["humidity"]["min"], self.config["humidity"]["max"]
                )
                pres_status = self.classify(
                    pres, self.config["pressure"]["min"], self.config["pressure"]["max"]
                )
                orient_status = self.classify_orientation(pitch, roll, yaw)

                self.log_data((
                    temp, hum, pres, pitch, roll, yaw,
                    temp_status, hum_status, pres_status, orient_status
                ))

                self.last_read_time = now

            self.display(
                temp, hum, pres, pitch, roll, yaw,
                (temp_status, hum_status, pres_status, orient_status)
            )

            time.sleep(0.1)


if __name__ == "__main__":
    app = SensorMonitor()
    app.run()