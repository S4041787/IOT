import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("../Task 3/envirotrack.db")

df = pd.read_sql_query("SELECT * FROM readings", conn)

# 1️ Line Graph
plt.figure()
plt.plot(df["timestamp"], df["temperature"])
plt.xticks(rotation=45)
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("temperature_line.png")

# 2️ Bar Chart
plt.figure()
status_counts = df["temp_status"].value_counts()

sns.barplot(x=status_counts.index, y=status_counts.values)
plt.title("Temperature Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("temperature_status_bar.png")

print("Graphs generated!")

# 3️ Scatter Plot
plt.figure()
hum_counts = df["humidity_status"].value_counts()

sns.barplot(x=hum_counts.index, y=hum_counts.values)
plt.title("Humidity Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("humidity_status_bar.png")