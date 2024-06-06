import pandas as pd

datas = pd.date_range("23/5/2000", periods = 3)

dicionario = {
	"cotacoes": [20, 30, 40],
	"volumes": [100, 50, 60],
	"datas": datas
}

df = pd.DataFrame(dicionario)
print(df)