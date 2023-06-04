# import csv

# def verificar_e_acrescentar_dados(features_file, vendas_file):
#     # Leitura do arquivo FeaturesDataSet.csv
#     with open(features_file, 'r') as arquivo_features:
#         leitor_features = csv.DictReader(arquivo_features)
#         dados_features = list(leitor_features)

#     # Leitura do arquivo vendas.csv
#     with open(vendas_file, 'r') as arquivo_vendas:
#         leitor_vendas = csv.DictReader(arquivo_vendas)
#         dados_vendas = list(leitor_vendas)

#     # Criação de um dicionário para mapear as linhas de vendas.csv
#     mapeamento_vendas = {(dados['loja_id'], dados['data_id']): dados for dados in dados_vendas}

#     # Verificação e acréscimo dos dados ao arquivo vendas.csv
#     for dados_feature in dados_features:
#         loja_id = dados_feature['Store']
#         data_id = dados_feature['Date']

#         if (loja_id, data_id) in mapeamento_vendas:
#             dados_venda = mapeamento_vendas[(loja_id, data_id)]
#             dados_venda['Temperature'] = dados_feature['Temperature']
#             dados_venda['Fuel_Price'] = dados_feature['Fuel_Price']
#             dados_venda['Unemployment'] = dados_feature['Unemployment']

#     # Escrita do arquivo vendas.csv atualizado
#     with open(vendas_file, 'w', newline='') as arquivo_vendas_atualizado:
#         cabecalho = ['loja_id', 'departamento_id', 'data_id', 'Weekly_Sales', 'feriado', 'Temperature', 'Fuel_Price', 'Unemployment']
#         escritor_vendas = csv.DictWriter(arquivo_vendas_atualizado, fieldnames=cabecalho)
#         escritor_vendas.writeheader()
#         escritor_vendas.writerows(dados_vendas)

#     print(f'Dados acrescentados ao arquivo "{vendas_file}" com sucesso.')

#     # Contagem do número de entradas no arquivo vendas.csv atualizado
#     num_entradas = len(dados_vendas)
#     print(f'O número de entradas no arquivo "vendas.csv" é: {num_entradas}')

# # Chamada da função para verificar e acrescentar os dados
# verificar_e_acrescentar_dados('D:/Escola/2022_23/AO/DataSet/FeaturesDataset.csv', 'D:/Escola/2022_23/AO/DataSet/vendasDataNoID.csv')
import csv

features_file = 'D:/Escola/2022_23/AO/DataSet/FeaturesDataset.csv'
sales_file = 'D:/Escola/2022_23/AO/DataSet/vendasDataNoIDCopy.csv'
output_file = 'D:/Escola/2022_23/AO/DataSet/vendasDataNoID.csv'

# Criar dicionário para armazenar os valores do arquivo FeaturesDataSet.csv
features_data = {}
with open(features_file, 'r') as f:
    features_reader = csv.DictReader(f)
    for row in features_reader:
        date = row['Date']
        store = row['Store']
        temperature = row['Temperature']
        fuel_price = row['Fuel_Price']
        unemployment = row['Unemployment']
        features_data[(date, store)] = (temperature, fuel_price, unemployment)

# Atualizar o arquivo vendas.csv e escrever o resultado no arquivo vendas_atualizado.csv
with open(sales_file, 'r') as f, open(output_file, 'w', newline='') as output:
    sales_reader = csv.DictReader(f)
    fieldnames = sales_reader.fieldnames + ['Temperature', 'Fuel_Price', 'Unemployment']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for row in sales_reader:
        date = row['data_id']
        store = row['loja_id']
        if (date, store) in features_data:
            temperature, fuel_price, unemployment = features_data[(date, store)]
            row['Temperature'] = temperature
            row['Fuel_Price'] = fuel_price
            row['Unemployment'] = unemployment
        writer.writerow(row)

print("Arquivo vendas_atualizado.csv foi gerado com sucesso.")

