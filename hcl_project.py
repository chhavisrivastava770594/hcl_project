import pandas as pd
# 1.Load Dataset
df=pd.read_csv("C:\\Users\\Chhav\\Downloads\\marketing_campaign.csv",sep="\t")
print(df)
#2. Data exploration(Inspecting rows,columns,shape, and data types)
df.head()
print(df.head(3))
df.tail()
print(df.tail())
df.sample(5,random_state=42)
print(df.sample(5,random_state=42))
df.shape
print(df.shape)
df.columns
print(df.columns)
df.dtypes
print(df.dtypes)
df.info()
df.describe()
print(df.describe())
df.describe(include='all')
print(df.describe(include='all'))
#3.Checking Values Counts,unique, categories,missing values, and duplicates
print(df['Education'].value_counts())
print(df['Marital_Status'].value_counts())
print(df['Education'].unique())
print(df['Marital_Status'].unique())
print(df.isna().sum())
print(df.duplicated().sum())
#4.Data Cleaning (Handling missing values ,wrong data types,duplicates,and categories)
#Fill missing values in income using median (due to outliers)
df['Income']= df['Income'].fillna(df['Income'].median())
print(df['Income'].isna().sum())
# Convert Dt_Customer from string/object to datatime format
df['Dt_Customer']=pd.to_datetime(df['Dt_Customer'],dayfirst=True)
print(df['Dt_Customer'].dtype)
# remove duplicate rows
df=df.drop_duplicates()
# Standardize inconsistent categories in Marital_Status
df['Marital_Status']=df['Marital_Status'].replace({'Alone':'Single','Absurd':'Single','YOLO':'Single'})
print(df['Marital_Status'].value_counts())
#Standardize education & Marital_Status and remove outliers
df['Education'] = df['Education'].replace({'2n Cycle': 'Master'})
df['Marital_Status'] = df['Marital_Status'].replace({'Absurd': 'Other', 'YOLO': 'Other'})
df = df[(df['Year_Birth'] >= 1940) & (df['Income'] < 600000)]
df = df.drop(columns=['Z_CostContact', 'Z_Revenue'], errors='ignore')
# 5.Feature Engineering(Creating new meaningful columns)
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
df['Total_Spending'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
print(df[['ID', 'Kidhome', 'Teenhome', 'Total_Children', 'Total_Spending']].head(5))
print(df[['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 'Total_Children', 'Total_Spending']].head(5))
#6. Columns and rows selection(using brackets,loc ,and iloc)
print(df.loc)
print(df.loc[2:7])
print(df.iloc)
print(df.iloc[2:7])
# --- 8. Basic Analysis ---
print("1. Average Income:", df['Income'].mean())
print("2. Average Total Spending:", df['Total_Spending'].mean())
print("3. Customers by Education:\n", df['Education'].value_counts())
print("4. Customers by Marital Status:\n", df['Marital_Status'].value_counts())
#7. Export Cleaned Dataset to CSV
df.to_csv('Final_cleaned_marketing.csv', index=False)
print("Data cleaning completed successfully!")