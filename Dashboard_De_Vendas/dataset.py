import json
import pandas as pd

# import dataframe
file = open(
    'Dashboard_De_Vendas\myData\myVendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

# Format Data
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

print(df)
file.close()
