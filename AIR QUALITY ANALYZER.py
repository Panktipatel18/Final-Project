# ==========================================
# Project: Air Quality Analysis
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("==========================================")
print("        AIR QUALITY ANALYSIS")
print("==========================================")

# ------------------------------------------
# 1. Create Dataset
# ------------------------------------------

print("\n--- 1. Creating Dataset ---")

np.random.seed(42)

dates = pd.date_range("2025-01-01", periods=100)

data = {
    "Date": dates,
    "PM2.5": np.random.randint(20, 151, 100),
    "PM10": np.random.randint(40, 201, 100),
    "NO2": np.random.randint(10, 81, 100),
    "Temperature": np.random.randint(15, 41, 100),
    "Humidity": np.random.randint(30, 91, 100)
}

df = pd.DataFrame(data)

print("Dataset created successfully!")

# ------------------------------------------
# 2. Display Dataset
# ------------------------------------------

print("\n--- 2. First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# ------------------------------------------
# 3. Statistical Summary
# ------------------------------------------

print("\n--- 3. Statistical Summary ---")
print(df.describe())

# ------------------------------------------
# 4. Find Pollution Information
# ------------------------------------------

print("\n--- 4. Pollution Information ---")

print("Average PM2.5:", df["PM2.5"].mean())
print("Maximum PM2.5:", df["PM2.5"].max())
print("Minimum PM2.5:", df["PM2.5"].min())

print("Average PM10:", df["PM10"].mean())
print("Maximum PM10:", df["PM10"].max())
print("Minimum PM10:", df["PM10"].min())

# ------------------------------------------
# 5. PM2.5 Trend Over Time
# ------------------------------------------

print("\n--- 5. PM2.5 Trend Over Time ---")

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["PM2.5"], label="PM2.5")

plt.xlabel("Date")
plt.ylabel("PM2.5 Level")
plt.title("PM2.5 Pollution Level Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("pm25_trend.png")
plt.show()

# ------------------------------------------
# 6. PM10 Trend
# ------------------------------------------

print("\n--- 6. PM10 Trend Over Time ---")

plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["PM10"], label="PM10")

plt.xlabel("Date")
plt.ylabel("PM10 Level")
plt.title("PM10 Pollution Level Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("pm10_trend.png")
plt.show()

# ------------------------------------------
# 7. Temperature vs PM2.5
# ------------------------------------------

print("\n--- 7. Temperature vs PM2.5 ---")

plt.figure(figsize=(8, 5))

plt.scatter(df["Temperature"], df["PM2.5"])

plt.xlabel("Temperature")
plt.ylabel("PM2.5")
plt.title("Temperature vs PM2.5")

plt.tight_layout()

plt.savefig("temperature_pm25.png")
plt.show()

# ------------------------------------------
# 8. Humidity vs PM2.5
# ------------------------------------------

print("\n--- 8. Humidity vs PM2.5 ---")

plt.figure(figsize=(8, 5))

plt.scatter(df["Humidity"], df["PM2.5"])

plt.xlabel("Humidity")
plt.ylabel("PM2.5")
plt.title("Humidity vs PM2.5")

plt.tight_layout()

plt.savefig("humidity_pm25.png")
plt.show()

# ------------------------------------------
# 9. Correlation
# ------------------------------------------

print("\n--- 9. Correlation Between Variables ---")

correlation = df[
    ["PM2.5", "PM10", "NO2", "Temperature", "Humidity"]
].corr()

print(correlation)

# ------------------------------------------
# 10. Simple Correlation Graph
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("correlation_matrix.png")
plt.show()

# ------------------------------------------
# 11. Final Analysis
# ------------------------------------------

print("\n==========================================")
print("           PROJECT ANALYSIS")
print("==========================================")

print("Total number of records:", len(df))

print("Average PM2.5:", round(df["PM2.5"].mean(), 2))
print("Average PM10:", round(df["PM10"].mean(), 2))
print("Average NO2:", round(df["NO2"].mean(), 2))
print("Average Temperature:", round(df["Temperature"].mean(), 2))
print("Average Humidity:", round(df["Humidity"].mean(), 2))

print("\nProject completed successfully!")