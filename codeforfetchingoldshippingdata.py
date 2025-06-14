import sqlite3
import csv
conn = sqlite3.connect('database_old.db')
table_name ="customer_shipping_table"
output_csv="shipping_data.csv"

cursor=conn.cursor()

cursor.execute(f"select * from {table_name}")

headers=[description[0] for description in cursor.description]


with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers) #header
    csv_writer.writerows(cursor) #rows

print(f"Data from '{table_name}' successfully exported to '{output_csv}'")
