lista = []

for i in range(5):
	preco_lucro = float(input("Digite o preço/lucro de uma empresa: "))
	lista.append(preco_lucro)

lista_ordenada = sorted(lista)

print(f"Os dois P/L menores foram {lista_ordenada[0]} e {lista_ordenada[1]}")