import pandas as pd

dicionario = {
	"nomes": ["Weg", "Petrobras", "Vale", "Petrobras", "Lojas Renner"],
	"tickers": ["WEGE3", "PETR3", "VALE3", "PETR4", "LREN3"],
	"cotacoes": [20, 30, 40, 12, 35],
	"preco_sobre_lucro": [25, 6, 12, 7, 25],
	"volume": [5000, 1000, 4000, 7000, 1200]
}

df = pd.DataFrame(dicionario)
df = df.set_index("tickers")
df.columns = ["nomes", "precos", "preco_sobre_lucro", "volume"]
df["lpa"] = df["precos"] / df["preco_sobre_lucro"]
df["cotacao_dolar"] = df["precos"] / 5.25 

df["ranking_lpa"] = df["lpa"].rank(method = "dense")

print(df)