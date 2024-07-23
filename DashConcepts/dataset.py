import pandas as pd

ecom_sales = pd.read_csv("ecom_sales.csv")
ecom_sales_new = ecom_sales.groupby('Country')['OrderValue'].agg(
    'sum').reset_index(name='Total Sales ($)')

# print(ecom_sales.head(5))
print(ecom_sales_new)
