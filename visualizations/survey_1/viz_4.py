import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cmap = matplotlib.cm.get_cmap('viridis')

df = pd.read_csv(r'survey_table_4_Feb_2021.csv', encoding_errors='ignore')
df = df[df['Unnamed: 0'].isin(['Less than 20', '20 to 99', '100 to 500', 'Over 500'])]
df.fillna(0, inplace=True)


df['Accomplishes more work per hour'] = [float(str(x).split('Note')[0]) if 'F:' not in str(x) else 0 for x in df['Accomplishes more work per hour'].values.tolist()]
df['Accomplishes about the same amount of work per hour'] = [float(str(x).split('Note')[0]) if 'F:' not in str(x) else 0 for x in df['Accomplishes about the same amount of work per hour'].values.tolist()]
df['Accomplishes less work per hour'] = [float(str(x).split('Note')[0]) if 'F:' not in str(x) else 0 for x in df['Accomplishes less work per hour'].values.tolist()]

fig = plt.figure(figsize=(10, 6))
ax = plt.barh(y=df['Unnamed: 0'].values.tolist(), width=df['Accomplishes less work per hour'].values.tolist(),
              height=0.3,
              color=cmap(0.1),
              alpha=0.7, edgecolor='k', linewidth=1,
              label='less work per hour', hatch='||')
ax = plt.barh(y=df['Unnamed: 0'].values.tolist(),
              width=df['Accomplishes about the same amount of work per hour'].values.tolist(),
              left=df['Accomplishes less work per hour'].values.tolist(),
              height=0.3,
              color=cmap(0.5),
              alpha=0.7,
              edgecolor='k', linewidth=1,
              label='same amount of work per hour', hatch='..')
ax = plt.barh(y=df['Unnamed: 0'].values.tolist(),
              width=df['Accomplishes more work per hour'].values.tolist(),
              height=0.3,
              left=[float(x) + float(y) for x, y in
                    zip(df['Accomplishes less work per hour'].values.tolist(),
                        df['Accomplishes about the same amount of work per hour'].values.tolist())],
              color=cmap(0.8),
              alpha=0.7,
              edgecolor='k', linewidth=1,
              label='more work per hour', hatch='xx')

for col, val_s in enumerate([df['Accomplishes less work per hour'],
                             df['Accomplishes about the same amount of work per hour'],
                             df['Accomplishes more work per hour']]):
    for row, val in enumerate(val_s):
        plt.text(col*40+0.1, row+0.17, f'{val} %')

plt.title('Accomplishment of work per hour in remote work scenario')
plt.xlabel('Percentage of people (a/c survey)')
plt.ylabel('Firm size (# of employees)')
plt.ylim(-0.5, 4.1)
plt.yticks(rotation=80)
plt.legend(loc='upper right')

plt.show()
