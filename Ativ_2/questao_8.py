# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd
df = pd.read_csv('Heart_Disease_Prediction.csv')

print("Primeiras linhas do dataset:")
print(df.head())
