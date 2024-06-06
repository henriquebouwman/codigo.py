import pandas as pd

datas = pd.date_range("23/5/2000", periods = 3)

dicionario = {
	"cotacoes": [20, 30, 40],
	"volumes": [100, 50, 60],
	"datas": datas
}

df = pd.DataFrame(dicionario)
df = df.set_index("datas")
print(df)