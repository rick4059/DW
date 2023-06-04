import pandas as pd

# Função para adicionar a coluna "venda_id" ao arquivo CSV
def adicionar_coluna_venda_id(arquivo_csv):
    # Carrega o arquivo CSV em um DataFrame do Pandas
    df = pd.read_csv(arquivo_csv)

    # Adiciona a coluna "venda_id" com valores de contador
    df.insert(0, "venda_id", range(1, len(df) + 1))

    # Salva o DataFrame atualizado no arquivo CSV
    novo_arquivo_csv = f'{arquivo_csv}'
    df.to_csv(novo_arquivo_csv, index=False)

    print(f'Coluna "venda_id" adicionada como a primeira coluna no arquivo "{arquivo_csv}".')

# Chamada da função para adicionar a coluna "venda_id" como a primeira coluna
adicionar_coluna_venda_id('D:/Escola/2022_23/AO/DataSet/vendasDataNoID.csv')
