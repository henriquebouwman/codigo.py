import pandas as pd

dicionario = {
	"tickers": ["WEGE3", "PETR3", "VALE3", "PETR4", "LREN3"],
	"cotacoes": [20, 30, 40, 12, 35],
	"nomes": ["Weg", "Petrobras", "Vale", "Petrobras", "Lojas Renner"],
	"preco_sobre_lucro": [25, 6, 12, 7, 25],
	"volume": [5000, 1000, 4000, 7000, 1200]
}

data = pd.DataFrame(dicionario)
data = data.set_index("tickers")
data.columns = ["preços", "nomes", "preco_sobre_lucro", "volume"]
primeira_linha = data.loc["WEGE3"]
primeira_coluna = data.loc[:, "preços"]

print(primeira_linha)
print("\n\n")
print(primeira_coluna)