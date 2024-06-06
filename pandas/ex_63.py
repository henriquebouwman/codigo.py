import pandas as pd
import yfinance as yf
from datetime import datetime

acao = ["ABEV3.SA", "WEGE3.SA", "RADL3.SA", "PCAR3.SA", "CASH3.SA"]

dados = yf.download(tickers = acao , start = "2018-12-31", end = datetime.now())
fechamento_ajustado = dados["Adj Close"]
print(fechamento_ajustado)