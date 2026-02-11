# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
import pandas as pd

df = pd.read_csv('Heart_Disease_Prediction.csv')
coluna_idade = df['Age']
print(coluna_idade.head())

filtro_colesterol = df[df['Cholesterol'] > 300]
print(filtro_colesterol.head())

resultado = df.loc[df['Age'] > 60, ['Age', 'Cholesterol', 'Heart Disease']]
print(resultado.head())
