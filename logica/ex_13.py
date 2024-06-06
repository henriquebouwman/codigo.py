nome = input("Qual seu nome? ")
print(f"Bem-vindo {nome}!")

carteira_1 = []
carteira_2 = []

for i in range(2):
	print(f"\n CARTEIRA {i+1}\n")
	for x in range(3):
		ticker = input(f"Digite o {x+1}º ticker da carteira {i+1}: ")
		if i == 0:
			carteira_1.append(ticker)
		if i == 1:
			carteira_2.append(ticker)

intersecao = set(carteira_1) & set(carteira_2)
print(f"A interseção entre as duas carteiras foi: {intersecao}")

diferenca = set(carteira_1) - set(carteira_2)
print(f"A diferença entre as duas carteiras foi: {diferenca}")

uniao = set(carteira_1) | set(carteira_2)
print(f"A união entre as duas carteiras foi: {uniao}")
