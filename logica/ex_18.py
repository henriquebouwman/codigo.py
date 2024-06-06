ticker = input("Digite o ticker: ")
if int(ticker[-1]) == 3:
	print(f"O ticker {ticker} é uma ação ON")
elif int(ticker[-1]) == 4:
	print(f"O ticker {ticker} é uma ação PN")
elif int(ticker[-1]) == 1:
	print(f"O ticker {ticker} é uma ação UNIT")
else:
	print(f"O ticker {ticker} digitado é inválido")