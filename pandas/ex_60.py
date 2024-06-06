import pandas as pd
import os
import matplotlib.pyplot as plt

diretorio_atual = os.getcwd()
os.chdir(diretorio_atual)

dados_petro = pd.read_excel("exercicio_receita_petro.xlsx", index_col= 'Data',skiprows= 4, usecols= ['Data','Receita Líquida 12 meses Consolidado Milhões', 'Convenção'], na_values= 'nd', decimal= ',') 

print(dados_petro)