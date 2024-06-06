nome = input("Digite o nome da empresa: ")
roe = float(input("Digite o ROE da empresa: "))
pl = float(input("Digite o P/L da empresa: "))
if roe > 0.15 and pl < 5:
	print(f"A empresa {nome} é recomendada para comprar!")
elif roe < 0.05 or pl < 0:
	print(f"A empresa {nome} não é recomendada para comprar, indicadores muito ruim!")
elif roe > 0.10 and pl > 30:
	print(f"A empresa {nome} não é recomendada para comprar, pois está muito cara!")
else:
	print(f"Não sou capaz de opinar sobre a empresa {nome}!")
