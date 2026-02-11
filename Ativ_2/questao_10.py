# 10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
import pandas as pd

df = pd.read_csv('Heart_Disease_Prediction.csv')
print(df.isnull().sum())
df_limpo = df.dropna()
df_limpo_col = df.dropna(subset=['Cholesterol'])

df_preenchido = df.fillna(0)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cholesterol'] = df['Cholesterol'].fillna(df['Cholesterol'].median())

df['BP'] = df['BP'].fillna(method='ffill')
