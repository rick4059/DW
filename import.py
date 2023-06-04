from ast import arg
import sys
import pyodbc
import csv

csv_file_path = 'D:/Escola/2022_23/AO/DataSet/venda.csv'
dsn = 'DataWarehouse'
table_name = '[StoresDW].[dbo].[venda]'
count = 0

# Crie uma conexão ODBC com o SQL Server usando autenticação do Windows
conn = pyodbc.connect('DSN=' + dsn + ';Trusted_Connection=yes;')

# Abra um cursor
cursor = conn.cursor()

# Leia os dados do arquivo CSV e insira-os na tabela
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values = ', '.join(["'"+ value +"'" for value in row])
        
        
        if(count == 0):
            count += 1
            columns = values
            columns = columns.replace("'", "")
            continue

        print("Columns : " + columns)    
        print("Values : " + values)
        
        sql_query = "INSERT INTO " + table_name + " ("+ columns +") VALUES("+ values +")"
        cursor.execute(sql_query)
        

# Confirme as alterações e feche a conexão
conn.commit()
conn.close()

print('Dados importados com sucesso.')
