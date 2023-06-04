# from ast import arg
# import sys
# import csv

# # Read data.csv
# data = {}
# with open('D:/Escola/2022_23/AO/DataSet/data.csv', 'r') as data_file:
#     reader = csv.DictReader(data_file)
#     for row in reader:
#         data[row['data_id']] = row
#     # print(data)
#     # sys.exit([arg])

# # Update venda.csv
# with open('D:/Escola/2022_23/AO/DataSet/vendasCopy.csv', 'r') as venda_file, open('D:/Escola/2022_23/AO/DataSet/vendas.csv', 'w', newline='') as updated_venda_file:
#     reader = csv.DictReader(venda_file)
#     writer = csv.DictWriter(updated_venda_file, fieldnames=reader.fieldnames)
#     writer.writeheader()
#     vendas_id = 1
#     for row in reader:
#         # print (row)
#         # sys.exit([arg])
#         dia, mes, ano = row['data_id'].split('/')

#         data_id = row['data_id']

#         for key, value in data.items():
#             if value['dia'] == str(dia) or value['mes'] == str(mes) or value['ano'] == str(ano):
#                 # print()
#                 # sys.exit([arg])
#                 updated_row = key
#                 # updated_row = {}
#                 updated_row['venda_id'] = vendas_id
#                 updated_row['loja_id'] = row['loja_id']
#                 updated_row['departamento_id'] = row['departamento_id']
#                 updated_row['data_id'] = data[key]['data_id']
#                 updated_row['Weekly_Sales'] = row['Weekly_Sales']
#                 updated_row['feriado'] = 'TRUE' if row['feriado'] == '1' else 'FALSE'
#                 writer.writerow(updated_row)
                
#         vendas_id = vendas_id + 1
import csv

# Leitura do arquivo CSV original
with open('D:/Escola/2022_23/AO/DataSet/vendasCopy.csv', 'r') as arquivo_original:
    leitor_csv = csv.DictReader(arquivo_original)
    dados_originais = list(leitor_csv)

# Leitura do arquivo CSV com as datas
with open('D:/Escola/2022_23/AO/DataSet/data.csv', 'r') as arquivo_datas:
    leitor_csv = csv.DictReader(arquivo_datas)
    dados_datas = list(leitor_csv)

# Atualização do arquivo CSV original com os IDs das datas correspondentes
for dados_orig in dados_originais:
    data_id_orig = dados_orig['data_id']
    for dados_data in dados_datas:
        dia = int(dados_data['dia'])
        mes = int(dados_data['mes'])
        ano = int(dados_data['ano'])
        if dia == int(data_id_orig[0:2]) and mes == int(data_id_orig[3:5]) and ano == int(data_id_orig[6:]):
            dados_orig['data_id'] = dados_data['data_id']
            break

# Escrita do arquivo CSV atualizado
with open('D:/Escola/2022_23/AO/DataSet/vendasDataNoID.csv', 'w', newline='') as arquivo_atualizado:
    cabecalho = ['venda_id','loja_id', 'departamento_id', 'data_id', 'Weekly_Sales', 'feriado', 'Temperature','Fuel_Price','Unemployment']
    escritor_csv = csv.DictWriter(arquivo_atualizado, fieldnames=cabecalho)
    escritor_csv.writeheader()
    escritor_csv.writerows(dados_originais)

print('Conversão concluída com sucesso.')


