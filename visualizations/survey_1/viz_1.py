import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_palette('viridis')
cmap = matplotlib.cm.get_cmap('viridis')

df = pd.read_csv(r'survey_table_1_Feb_2021.csv')
df.dropna(inplace=True)

# need to rearrange the data
# both sexes at row 0, men at 1 and women at 2
data = {'Both sexes': [float(v) for idx, v in enumerate(df.iloc[0].values.tolist()) if idx > 0],
        'Men': [float(v) for idx, v in enumerate(df.iloc[1].values.tolist()) if idx > 0],
        'Women': [float(v) for idx, v in enumerate(df.iloc[2].values.tolist()) if idx > 0],
        'Index Title': df.T.index[1:]}

rearranged_df = pd.DataFrame(data=data)
print(rearranged_df)

base_data = {
    'Percentage': [data[grp][idx] for grp in ['Both sexes', 'Men', 'Women'] for idx in range(len(df.T.index[1:]))],
    'Group': [grp for grp in ['Both sexes', 'Men', 'Women'] for _ in range(len(df.T.index[1:]))],
    'Preference': [v for _ in range(3) for v in df.T.index[1:]]
}
base_df = pd.DataFrame(data=base_data)
# fig = px.bar(base_df, x='Preference', y='Percentage', color='Group')
# fig.show()

print(base_df)
plt.figure(figsize=(10, 10))
ax = sns.barplot(x='Preference', hue='Group', y='Percentage', data=base_df,
                 order=np.unique(base_df['Preference'].values.tolist()), alpha=0.7,
                 linewidth=1, dodge=True, ci=None, edgecolor='k')
age_grps, counts = np.unique(base_df['Preference'].values.tolist(), return_counts=True)

bars = ax.patches
pattern = ['//', '..', 'xx']
hatches = np.repeat(pattern, len(np.unique(base_df['Preference'].values.tolist())))

for pat, bar in zip(hatches, bars):
    bar.set_hatch(pat)

for p in ax.patches:
    height = p.get_height()
    try:
        txt = f'{int(height)} %'
    except:
        txt = '0 %'
    ax.text(p.get_x()+0.1, height+2, txt,
            fontsize=12, rotation=90)

ax.set_title('Preference of different groups', fontsize=20)
ax.set_ylabel('Percentage', fontsize=15)
ax.set_xlabel('Preference', fontsize=15)
ax.set_ylim([0, 60])
ax.legend()
plt.tight_layout()
plt.show()
