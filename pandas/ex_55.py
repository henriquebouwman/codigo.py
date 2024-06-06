import pandas as pd

dicionario = {
	"nomes": ["Weg", "Petrobras", "Vale", "Petrobras", "Lojas Renner"],
	"tickers": ["WEGE3", "PETR3", "VALE3", "PETR4", "LREN3"],
	"cotacoes": [20, 30, 40, 12, 35],
	"preco_sobre_lucro": [25, 6, 12, 7, 25],
	"volume": [5000, 1000, 4000, 7000, 1200]
}

data = pd.DataFrame(dicionario)
data = data.set_index("tickers")
data.columns = ["nomes", "precos", "preco_sobre_lucro", "volume"]
data["lpa"] = data["precos"] / data["preco_sobre_lucro"]

maior_lucro = data["lpa"].max() 
menor_lucro = data["lpa"].min() 

acao_maior_lucro = data[data["lpa"] == maior_lucro]
acao_maior_lucro = acao_maior_lucro.iat[0, 0]

acao_pior_lucro = data.loc[data["lpa"] == menor_lucro]
acao_pior_lucro = acao_pior_lucro.iat[0, 0]

#acao_maior_lucro = data.loc[data["Lucro por ação"] == maior_lucro, "nomes"]
#acao_pior_lucro = data.loc[data["Lucro por ação"] == menor_lucro, "nomes"]

print(f"A ação com MAIOR lucro é a {acao_maior_lucro} com {maior_lucro} de lucro por ação.")
print(f"A ação com MENOR lucro é a {acao_pior_lucro} com {menor_lucro} de lucro por ação.")