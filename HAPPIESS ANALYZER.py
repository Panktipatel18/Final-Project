import pandas as pd
import matplotlib.pyplot as plt

print("Welcome to World Happiness Data Analysis")
print("-----------------------------------------")

# 1. Create the dataset

data = {
    "Country": [
        "Finland",
        "Denmark",
        "Iceland",
        "Switzerland",
        "Netherlands",
        "Norway",
        "Sweden",
        "Luxembourg",
        "New Zealand",
        "Canada"
    ],

    "Happiness Score": [
        7.8,
        7.6,
        7.5,
        7.5,
        7.4,
        7.3,
        7.3,
        7.2,
        7.1,
        7.0
    ],

    "Economy (GDP per Capita)": [
        1.34,
        1.38,
        1.37,
        1.40,
        1.36,
        1.39,
        1.35,
        1.42,
        1.30,
        1.33
    ],

    "Social support": [
        1.59,
        1.57,
        1.58,
        1.52,
        1.52,
        1.54,
        1.49,
        1.48,
        1.47,
        1.44
    ],

    "Health": [
        0.96,
        0.95,
        0.97,
        0.94,
        0.95,
        0.96,
        0.94,
        0.93,
        0.92,
        0.91
    ]
}

df = pd.DataFrame(data)

# 2. Display first 5 rows

print("\nFirst 5 rows of the dataset:")
print(df.head())

# 3. Display dataset information

print("\nDataset Information:")
print(df.info())

# 4. Check missing values

print("\nMissing values in each column:")
print(df.isnull().sum())

# Remove missing values if any
df = df.dropna()

# 5. Basic Statistics

print("\nBasic Summary Statistics:")
print(df.describe())

# 6. Find the country with highest happiness score

highest = df.loc[df["Happiness Score"].idxmax()]

print("\nCountry with highest happiness score:")
print(highest["Country"])
print("Happiness Score:", highest["Happiness Score"])

# 7. Find the country with lowest happiness score

lowest = df.loc[df["Happiness Score"].idxmin()]

print("\nCountry with lowest happiness score:")
print(lowest["Country"])
print("Happiness Score:", lowest["Happiness Score"])

# 8. Correlation Matrix

print("\nCorrelation Matrix:")

numeric_df = df.select_dtypes(include=["number"])
correlation = numeric_df.corr()

print(correlation)

# 9. Display Correlation Matrix as a graph

plt.figure(figsize=(10, 7))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix of Happiness Factors")

plt.tight_layout()

plt.savefig("correlation_matrix.png")

plt.show()

# 10. GDP per Capita vs Happiness Score

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Economy (GDP per Capita)"],
    df["Happiness Score"]
)

plt.title("GDP per Capita vs Happiness Score")

plt.xlabel("GDP per Capita")

plt.ylabel("Happiness Score")

plt.grid(True)

plt.tight_layout()

plt.savefig("gdp_vs_happiness.png")

plt.show()

# 11. Social Support vs Happiness Score

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Social support"],
    df["Happiness Score"]
)

plt.title("Social Support vs Happiness Score")

plt.xlabel("Social Support")

plt.ylabel("Happiness Score")

plt.grid(True)

plt.tight_layout()

plt.savefig("social_support_vs_happiness.png")

plt.show()

# 12. Happiness Score of Countries

plt.figure(figsize=(10, 6))

plt.bar(
    df["Country"],
    df["Happiness Score"]
)

plt.title("Happiness Score of Countries")

plt.xlabel("Country")

plt.ylabel("Happiness Score")

plt.xticks(rotation=45)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("country_happiness.png")

plt.show()

print("\n-----------------------------------------")
print("Analysis complete!")
print("All graphs have been saved successfully.")