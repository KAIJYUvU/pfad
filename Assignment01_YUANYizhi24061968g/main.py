import pandas as pd
import matplotlib.pyplot as plt

file_path = 'marine-recent-en.csv'
data = pd.read_csv(file_path)

data['Sampling Date'] = pd.to_datetime(data['Sampling Date'])

selected_columns = data[['Sampling Date', 'Dissolved Oxygen (mg/L)', '5-day Biochemical Oxygen Demand (mg/L)']]

selected_columns.set_index('Sampling Date', inplace=True)

plt.figure(figsize=(12, 8))
plt.plot(selected_columns.index, selected_columns['Dissolved Oxygen (mg/L)'], marker='o', linestyle='None', color='b', label='Dissolved Oxygen (mg/L)')
plt.plot(selected_columns.index, selected_columns['5-day Biochemical Oxygen Demand (mg/L)'], marker='s', linestyle='None', color='r', label='5-day Biochemical Oxygen Demand (mg/L)')
plt.title('Dissolved Oxygen and 5-day Biochemical Oxygen Demand', fontsize=16)
plt.xlabel('Sampling Date', fontsize=14)
plt.ylabel('Value (mg/L)', fontsize=14)
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()