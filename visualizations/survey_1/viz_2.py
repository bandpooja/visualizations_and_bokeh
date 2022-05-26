import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_palette('viridis')
cmap = matplotlib.cm.get_cmap('viridis')

df = pd.read_csv(r'survey_table_2_Feb_2021.csv', encoding_errors='ignore')
df.dropna(inplace=True)

print(df)
df_overall = df[df['Unnamed: 0'].str.contains('Overall')]
df_ontario = df[df['Unnamed: 0'].str.contains('Ontario')]
df_family = df[df['Unnamed: 0'].str.contains('arried')]
print(df_overall)
print(df_ontario)
print(df_family)


plt.figure(figsize=(20, 10))

labels = df_overall.columns.values.tolist()[1:]
per = df_overall.iloc[0].values.tolist()[1:]
type_ = df_overall.iloc[0].values.tolist()[0]

plt.subplot(1, 1, 1)
ax1, _, autotexts = plt.pie(x=[float(x) for x in per], startangle=90,
                           autopct='%1.1f%%', textprops={'fontsize': 14}, radius=0.95)

pattern = ['//', '..', 'xx']
hatches = pattern

for hatch, wedge in zip(hatches, ax1):
    wedge.set_hatch(hatch)
    wedge.set_alpha(0.7)
    wedge.set_edgecolor('k')

for text in autotexts:
    text.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='k'))

labels_o = df_ontario.columns.values.tolist()[1:]
per_o = df_ontario.iloc[0].values.tolist()[1:]
type_o = df_ontario.iloc[0].values.tolist()[0]

ax2, _, autotexts = plt.pie(x=[float(x) for x in per_o], startangle=90,
                           autopct='%1.1f%%', textprops={'fontsize': 14}, radius=0.43)

pattern = ['//', '..', 'xx']
hatches = pattern

for hatch, wedge in zip(hatches, ax2):
    wedge.set_hatch(hatch)
    wedge.set_alpha(0.9)
    wedge.set_edgecolor('k')

for text in autotexts:
    text.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='k'))


plt.title(f'Work efficiency {type_}', fontsize=20)
labels = [f'{lbl.replace("/common-law", "").replace(" or common-law", "")} - ' + '$\\bf{Ontario}$' + f' {str(p)} %' for lbl, p in zip(labels_o, per_o)]
labels += [f'{lbl.replace("/common-law", "").replace(" or common-law", "")} - ' + '$\\bf{Canada}$' + f' {str(p)} %' for lbl, p in zip(labels, per)]

labels = labels[3:]
plt.legend(ax2, labels, loc="upper right")
# plt.legend(ax1, labels, loc="upper right")

plt.tight_layout()
plt.show()
