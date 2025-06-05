import chardet
#load the data
with open(r'C:\Users\USER\Downloads\dataset1\Sample - Superstore.csv','rb') as f:
    result = chardet.detect(f.read(10000))
#view first few rows
    print(result)

import pandas as pd
df = pd.read_csv( r'C:\Users\USER\Downloads\dataset1\Sample - Superstore.csv',
    encoding='ISO-8859-1')
print(df.head())

#understanding dataset structure
print(df.info())          # Column names, data types, null values
print(df.describe())      # Summary statistics (numerical)
print(df.columns)         # All column names

#clean the data
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')   #converts date to datetime

df = df.drop(columns=['Postal Code'], errors='ignore')  # drop unnecessary columns

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Month-Year'] = df['Order Date'].dt.to_period('M') #create new columns

#analysis
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print(df.groupby('Region')['Sales'].sum()) #sales by region
top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(5)
print(top_products) #top 5 products by profit
monthly_sales = df.groupby('Month-Year')['Sales'].sum()
print(monthly_sales) #monthly sales trend

#export clean data for power bi
df.to_excel("Cleaned_Superstore_Data.xlsx", index=False)

