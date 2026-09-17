# ==========================================
# Project: Stock Market Analysis
# ==========================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf

# Set up seaborn style for clean plots
sns.set_theme(style="darkgrid")

# 1. Load Dataset
stock_symbol = "AAPL"
start_date = "2023-01-01"
end_date = "2026-01-01"

print(f"Download historical stock price data for apple (AAPL)...")
df = yf.download("AAPL", start="2023-01-01", end="2026-01-01")

# Quick check on the data
print("\nFirst 5 rows of the dataset:")
print(df.head())

# If multi-index columns occur in newer yfinance versions, flatten them
if isinstance(df.columns, pd.MultiIndex):
  df.columns = df.columns.get_level_values(0)

# 2. Data Manipulation / Calculations
# Calculating Moving Averages (e.g., 50-day and 200-day MA)
df["MA50"] = df["Close"].rolling(window=50).mean()
df["MA200"] = df["Close"].rolling(window=200).mean()

# Daily Returns calculation (just a cool extra metric)
df["Daily_Return"] = df["Close"].pct_change()

print("\nBasic Summary Statistics:")
print(df.describe())

# 3. Visualizations

# Plot 1: Stock Price with Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"], label="Close Price", color="blue", alpha=0.6)
plt.plot(
    df.index, df["MA50"], label="50-Day Moving Average", color="orange", lw=1.5
)
plt.plot(
    df.index, df["MA200"], label="200-Day Moving Average", color="red", lw=1.5
)

plt.title(f"{stock_symbol} Stock Price & Moving Averages", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.legend()
plt.show()

# Plot 2: Trading Volume Over Time
plt.figure(figsize=(12, 4))
plt.bar(df.index, df["Volume"], color="purple", alpha=0.5, width=2)
plt.title(f"{stock_symbol} Trading Volume", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Volume", fontsize=12)
plt.show()

# Plot 3: Distribution of Daily Returns using Seaborn
plt.figure(figsize=(8, 5))
sns.histplot(
    df["Daily_Return"].dropna(), bins=50, kde=True, color="green"
)
plt.title(f"{stock_symbol} Daily Returns Distribution", fontsize=14)
plt.xlabel("Daily Return", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

print("\nAnalysis completed successfully!")