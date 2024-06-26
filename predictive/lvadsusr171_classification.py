# -*- coding: utf-8 -*-
"""LVADSUSR171_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/103sCdp7_9YXo1321ED8-Y3U42F8dxtzV
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier

import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("/content/winequality-red.csv")
df.head()

df.shape

df.info()

df.describe(include="all")

df.columns

df.rename(columns={'fixed acidity':'fixed_acidity'}, inplace=True)
df.rename(columns={'volatile acidity':'volatile_acidity'}, inplace=True)
df.rename(columns={'citric acid':'citric_acid'}, inplace=True)
df.rename(columns={'residual sugar':'residual_sugar'}, inplace=True)
df.rename(columns={'free sulfur dioxide':'free_sulfur_dioxide'}, inplace=True)
df.rename(columns={'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)

df.columns

df.isnull().sum()

df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.duplicated().sum()

df.dtypes

df.quality.value_counts()

"""**UNIVARIATE ANALYSIS**"""

for column in df.select_dtypes(include={'float64','int64'}).columns:
  plt.figure(figsize=(10,5))
  sns.histplot(df[column])
  plt.title(f'Histogram of {column}')
  plt.xlabel(column)
  plt.ylabel('Frequency')
  plt.show()

"""**BIVARIATE ANALYSIS**"""

numerical_columns=df.select_dtypes(include={'float64','int64'}).columns
numerical_columns

for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

#correlation matrix
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

plt.figure(figsize=(14, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

"""**NULL VALUE TREATMENT**"""

df.isnull().sum()

df.fixed_acidity=df.fixed_acidity.fillna(df.fixed_acidity.median())
df.volatile_acidity=df.volatile_acidity.fillna(df.volatile_acidity.median())
df.citric_acid=df.citric_acid.fillna(df.citric_acid.median())
df.residual_sugar=df.residual_sugar.fillna(df.residual_sugar.median())
df.chlorides=df.chlorides.fillna(df.chlorides.median())
df.free_sulfur_dioxide=df.free_sulfur_dioxide.fillna(df.free_sulfur_dioxide.median())
df.sulphates=df.sulphates.fillna(df.sulphates.median())

df.isnull().sum()

#Outlier boxplot
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for column in numerical_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

df.dtypes

#random forest

#train test split

X=df.drop(columns=['quality'])
y=df['quality']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
model=RandomForestClassifier(n_estimators=80)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# Recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

# F1-score
#f1_score = f1_score(y1_test, y1_pred)
#print("F1-score:", f1_score)

# Generate a classification report
print(classification_report(y_test, y_pred))

# Generate a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu", fmt="d", cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

#knn

X1 = df.drop(columns = ['quality'])
y1 = df['quality']

model =  KNeighborsClassifier(n_neighbors=2)

model.fit(X1, y1)
y1_pred = model.predict(X1)
df = [round(value) for value in y1_pred]

accuracy = accuracy_score(y1,df)
print("Model Prediction Accuracy: %.2f%%" % (accuracy * 100.0))
print("\n")

# Accuracy
accuracy = accuracy_score(y1, y1_pred)
print("Accuracy:", accuracy)

# Precision
precision = precision_score(y1, y1_pred)
print("Precision:", precision)

# Recall
recall = recall_score(y1, y1_pred)
print("Recall:", recall)

# F1-score
#f1_score = f1_score(y1_test, y1_pred)
#print("F1-score:", f1_score)







