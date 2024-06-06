import pandas as pd
import yfinance as yf
from datetime import datetime

acao = "^BVSP"

dados = yf.download(tickers = acao , start = "1994-06-01", end = datetime.now())
fechamento_ajustado = dados["Adj Close"]

print(fechamento_ajustado)

rentabilidade = fechamento_ajustado.iloc[-1]/fechamento_ajustado.iloc[0] - 1

print(rentabilidade)