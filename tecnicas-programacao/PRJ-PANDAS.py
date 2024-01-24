import pandas as pd

#01 Leitura de Arquivos CSV
df1 = pd.read_csv('jobs_in_data-1.csv')
df2 = pd.read_csv('jobs_in_data-2.csv')

#02 Criação de Colunas
df1['data_file'] = '1'
df2['data_file'] = '2'

#03 Mesclagem de Data Frames
df = pd.concat([df1, df2], ignore_index=True)
df.tail()

#0 Identificação dos Tipos das Colunas
df.dtypes

#0 Preenchimento de Valores Faltantes
moeda_vazia = df[df['salary_currency'].isnull()]

uds_vazio = moeda_vazia['company_location'] == 'United States'
df.loc[uds_vazio.index, 'salary_currency'] = 'USD'

cad_vazio = moeda_vazia['company_location'] == 'Canada'
df.loc[cad_vazio.index, 'salary_currency'] = 'CAD'

gbp_vazio = moeda_vazia['company_location'] == 'United Kingdom'
df.loc[gbp_vazio.index, 'salary_currency'] = 'GBP'

df['salary_currency'].fillna('EUR', inplace=True)