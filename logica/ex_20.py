lista = []
for i in range(5):
	cotacao = float(input("Digite uma cotação: "))
	lista.append(cotacao)

lista_ordenada = sorted(lista)
print(f"A maior cotação foi R$ {lista_ordenada[-1]} e a menor foi R$ {lista_ordenada[0]}")
