import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# Display basic dataset information
print('--- Dataset Info ---')
print(df.info())
print('\n--- First 5 Rows ---')
print(df.head())

# Set visual style for Seaborn
sns.set_theme(style='whitegrid')

# 1. Survival Rate by Gender
plt.figure(figsize=(6, 4))
sns.barplot(x='sex', y='survived', data=df, errorbar=None)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()

# 2. Survival Rate by Passenger Class (pclass)
plt.figure(figsize=(6, 4))
sns.barplot(x='pclass', y='survived', data=df, errorbar=None)
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.show()

# 3. Age Distribution of Passengers
plt.figure(figsize=(8, 4))
sns.histplot(df['age'].dropna(), kde=True, bins=30, color='teal')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 4. Survival Rate by Class and Gender
plt.figure(figsize=(8, 5))
sns.barplot(x='pclass', y='survived', hue='sex', data=df, errorbar=None)
plt.title('Survival Rate by Class and Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.legend(title='Gender')
plt.show()