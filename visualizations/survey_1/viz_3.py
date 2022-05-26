import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_palette('viridis')
cmap = matplotlib.cm.get_cmap('viridis')

df = pd.read_csv('survey_table_3_Feb_2021.csv')
issues = df['Unnamed: 0'].values.tolist()
percent = df['percent'].values.tolist()

bubble_cen = {}
bubble_size = {}
for iss_, per in zip(issues, percent):
    if iss_ == 'Lack of interaction with co-workers':
        bubble_cen[iss_] = (0.5, -0.5)
    elif iss_ == 'Need to do additional work to get things done':
        bubble_cen[iss_] = (2.1, 4.1)
    elif iss_ == "Caring for children / other family members":
        bubble_cen[iss_] = (0.15, 12)
    elif iss_ == "Other reasons / don't know":
        bubble_cen[iss_] = (4.75, -1)
    elif iss_ == "Accessing work-related information or devices":
        bubble_cen[iss_] = (7.5, 3)
    elif iss_ == "Inadequate physical workspace":
        bubble_cen[iss_] = (8.80, -0.75)
    elif iss_ == "Internet speed":
        bubble_cen[iss_] = (8.50, 5.75)

    bubble_size[iss_] = per*500


pattern = ['//', '..', 'xx', '++', 'OO', '||', '*', '--']
fig, ax = plt.subplots()

legend_labels = []
tx = []
for hatch, px_k in zip(pattern, bubble_cen.keys()):
    ax = plt.scatter(x=bubble_cen[px_k][0], y=bubble_cen[px_k][1], s=bubble_size[px_k],
                     c=[cmap((bubble_size[px_k]*4)/(100*500))],
                     alpha=0.7, linewidth=1, edgecolor='k', hatch=hatch)
    legend_labels.append(mpatches.Patch(facecolor=cmap((bubble_size[px_k]*4)/(100*500)),
                                        alpha=0.7, hatch=hatch, edgecolor='k')
                         )
    text = plt.text(x=bubble_cen[px_k][0]-0.5, y=bubble_cen[px_k][1], s=f'{str(bubble_size[px_k]/500)}%')
    text.set_bbox(dict(facecolor='white', alpha=1, edgecolor='k'))

plt.legend(legend_labels, bubble_cen.keys(), prop={'size': 8})
plt.xlim(-1.5, 10)
plt.ylim(-6, 17)
plt.title('Reason for inefficiency while working from home')
plt.axis('off')
plt.show()
