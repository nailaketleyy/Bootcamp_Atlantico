# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes?
import pandas as pd

df_heart_1 = pd.read_csv('Heart_Disease_Prediction.csv')
df_heart_2 = pd.read_csv('Heart Attack Data Set.csv')

df_vertical = pd.concat([df_heart_1, df_heart_2], axis=0, sort=False)
print(f"Colunas resultantes: {df_vertical.columns}")

df_info_basica = df_heart_1[['Age', 'Sex', 'BP']].iloc[:5]
df_info_clinica = df_heart_1[['Cholesterol', 'Heart Disease']].iloc[:5]

df_horizontal = pd.concat([df_info_basica, df_info_clinica], axis=1)
