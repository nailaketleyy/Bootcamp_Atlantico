# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

import pandas as pd

df = pd.read_csv('Heart_Disease_Prediction.csv')
col = 'Cholesterol'

Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers = df[(df[col] < lim_inf) | (df[col] > lim_sup)]
print(f"Outliers detectados por IQR: {len(outliers)}")
