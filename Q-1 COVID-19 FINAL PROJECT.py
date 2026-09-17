import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Standard URL for the Our World in Data COVID-19 dataset
url = 'https://www.kaggle.com/datasets/imdevskp/corona-virus-report'
local_file = 'covid_data.csv'

print('Loading COVID-19 dataset...')

try:
  # engine='python' and on_bad_lines='skip' prevent tokenizer and parsing errors
  df = pd.read_csv(url, engine='python', on_bad_lines='skip')
  print('Successfully loaded dataset from the web!')
except Exception as e:
  print(f'Web load failed ({e}). Attempting to load from local file...')
  try:
    df = pd.read_csv(local_file, engine='python', on_bad_lines='skip')
    print('Successfully loaded dataset from local file!')
  except Exception as local_err:
    print(f'Error loading local file: {local_err}')
    exit()

# Filter data for India (change 'India' if you want a different country)
if 'location' in df.columns:
  india = df[df['location'] == 'India'].copy()
else:
  print("Warning: 'location' column not found. Using full dataset.")
  india = df.copy()

# Select columns for correlation analysis safely
cols_to_check = [
    'total_cases',
    'total_deaths',
    'people_vaccinated',
    'people_fully_vaccinated',
    'stringency_index',
]
available_cols = [col for col in cols_to_check if col in india.columns]

if available_cols:
  # Calculate correlation matrix
  correlation_data = india[available_cols].corr()

  print('\nCorrelation between COVID-19 variables:')
  print(correlation_data)

  # 18. CORRELATION HEATMAP
  plt.figure(figsize=(8, 6))
  sns.heatmap(
      correlation_data, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5
  )
  plt.title('COVID-19 Variables Correlation Heatmap - India')
  plt.tight_layout()
  plt.show()
else:
  print('Required columns for correlation were not found in the dataset.')

print('\nProject completed successfully!')