import pandas as pd
import os

diretorio_atual = os.getcwd()
os.chdir(diretorio_atual)

dados_csv = pd.read_csv('exercicio_dre.csv', 
	sep= ';', 
	encoding= 'ISO-8859-1', 
	index_col= 'DT_REFER', 
	decimal= ',', 
	usecols=['DT_REFER', 'DENOM_CIA', 'ESCALA_MOEDA', 'ORDEM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA'])

print(dados_csv)