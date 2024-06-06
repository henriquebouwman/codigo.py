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
volume_total = data["volume"].sum()


print(volume_total)