# -*- coding: utf-8 -*-
"""LVADSUSR171_Nithikksha_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19sgfpIN-f3dUGsxVHJrl6hmE7DsyFNjf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
import warnings as wr
wr.filterwarnings('ignore')

#1a
data=pd.read_csv("/content/Final Dataset - IPL.csv")
data.head()

# @title first_ings_wkts

from matplotlib import pyplot as plt
data['first_ings_wkts'].plot(kind='hist', bins=20, title='first_ings_wkts')
plt.gca().spines[['top', 'right',]].set_visible(False)

#1b
data.shape

"""It has 74 rows and 20 columns"""

data.dtypes

data.isnull().sum()

"""This dataset does not have any missing values"""

#2a
data.isnull().sum()

"""This dataset does not have any missing values."""

#2b
data.duplicated().sum()

"""This dataset does not have any duplicates."""

data.drop_duplicates(inplace=True) #dropping duplicates

#3a
data.describe()

#median
median=data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']].median()
print(median)

#mode
mode=data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']].mode()
print(mode)

#variance
variance=data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']].var()
print(variance)

#range
range=data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']].max()-data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']].min()
print(range)

#4
#Histogram
from matplotlib import pyplot as plt
data['first_ings_score'].plot(kind='hist', bins=20, title='first_ings_score')
plt.gca().spines[['top', 'right',]].set_visible(False)

#scatter plot
from matplotlib import pyplot as plt
data.plot(kind='scatter', x='first_ings_score', y='first_ings_wkts', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

#boxplot
plt.boxplot(data['highscore'])

"""From the above two graphs there are no outliers"""

#bargraph
from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('venue').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

#pie chart
from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('won_by').size().plot(kind='pie', autopct="%1.1f%%")
plt.gca().spines[['top', 'right',]].set_visible(False)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data.venue=le.fit_transform(data.venue)
data.toss_decision=le.fit_transform(data.toss_decision)

#5
correl_mat = data[['first_ings_score','second_ings_score','venue','toss_decision']]
c = correl_mat.corr()
sns.heatmap(c, annot = True)

"""The first inning score and toss decision has high correlation.
venue has negative correlation on first innings.
"""

#6
plt.boxplot(data[['match_id',	'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'second_ings_wkts',	'margin',	'highscore']])

"""
'first_ings_score',	'first_ings_wkts',	'second_ings_score',	'margin',	these columns have outliers in this datset and it should be treated."""

data.head()

#8
from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('player_of_the_match').size().head(10).plot(kind='barh')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""dinesh karthik, david miller and avesh khan are the most player of the match"""

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby(['top_scorer','won_by']).size().head(5).plot(kind='pie', autopct="%1.1f%%")
plt.gca().spines[['top', 'right',]].set_visible(False)

"""In this case even when the player scored most runs the victory is greater in wickets."""

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby(['best_bowling','won_by']).size().head(5).plot(kind='pie', autopct="%1.1f%%")
plt.gca().spines[['top', 'right',]].set_visible(False)

"""The most wins is based on the wickets."""

#7
from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('player_of_the_match').size().sort_values().head(10).plot(kind='barh')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby(['team1','team2']).size().head(10).plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['won_by'].value_counts()
    for x_label, grp in data.groupby('venue')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('venue')
_ = plt.ylabel('won_by')

#9
from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(data['won_by'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(data, x='match_id', y='won_by', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

# @title match_id vs toss_decision

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['match_id']
  ys = series['toss_decision']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = data.sort_values('match_id', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('won_by')):
  _plot_series(series, series_name, i)
  fig.legend(title='won_by', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('match_id')
_ = plt.ylabel('toss_decision')

"""The match won by 50% batting and 50% bowling team
The match is more won by wickets.
The most wins is mainly based on the wickets.
The most player of the match is all rounder
"""





