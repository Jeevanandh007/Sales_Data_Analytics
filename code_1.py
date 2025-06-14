import pandas as pd

df= pd.read_csv('customer_orders.csv')

#print(df.head())

#print(df.columns)

df_unique_columns= df[['order number', 'employee id', 'employee name',
       'employee_job_title', 'order date', 'order type', 'customer type',
       'cust id', 'customer name', 'prod category',   
       'prod number', 'prod_name', 'quantity', 'price', 'order total']]

#print(df_unique_columns)

#print(df_unique_columns)

df_clean_columns=df_unique_columns.reset_index()
df_clean_columns.columns=[col.replace(' ', '') for col in df_clean_columns.columns]
#print(df_clean_columns.head())

#print(df_clean_columns[df.duplicated()])

df_clean_columns_rows=df_clean_columns.drop_duplicates(subset=['ordernumber','orderdate'])

df_clean_columns_rows.head()



##### Insert Data into SQL

import sqlite3 
conn =sqlite3.connect('database.db')

df_clean_columns_rows.to_sql('customer_orders_table', conn, if_exists='replace', index=False)