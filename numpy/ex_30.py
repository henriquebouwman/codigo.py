import numpy as np

lista_cotacoes = []

for i in range(3):
	cotacao = float(input(f"Digite a {i + 1}ª cotação: "))
	lista_cotacoes.append(cotacao)

array = np.array(lista_cotacoes)

print(array)