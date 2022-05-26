import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'ops_workforce_demographic_dataset_-_2015_to_2021_english.csv',
                 skiprows=2, encoding="ISO-8859-1")
df.dropna(inplace=True)
print(df.columns)
print(df)
dates = df['Date'].values.tolist()
less_than_6_leaves = df['Average # Staff with Fewer than 6 Sick Credit Days Taken (As of Last Complete Calendar Year)'].values.tolist()
more_than_6_leaves = df['Average # Staff with 6 or More Sick Credit Days (As of Last Complete Calendar Year)'].values.tolist()

plt.plot(dates, less_than_6_leaves, label='# less than 6 leaves', color='tab:blue')
plt.plot(dates, [np.mean(less_than_6_leaves) for _ in less_than_6_leaves], linestyle='--', color='tab:blue',
         label='mean - # less than 6 leaves')

plt.plot(dates, more_than_6_leaves, label='# more than 6 leaves', color='tab:orange')
plt.plot(dates, [np.mean(more_than_6_leaves) for _ in more_than_6_leaves], linestyle='--', color='tab:orange',
         label='mean - # more than 6 leaves')
plt.title('People and their leaves')
plt.xlabel('Survey Date')
plt.ylabel('# of Full Time Employees')
plt.grid()
plt.xticks(rotation=20)
plt.legend()
plt.show()
