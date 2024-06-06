import numpy as np

lista_numeros = []

while len(lista_numeros) < 6:
	numero = np.random.randint(0, 60, 1)[0]
	if numero not in lista_numeros:
		lista_numeros.append(numero)

lista_ordenada = sorted(lista_numeros)
probabilidade = "{:.2%}".format(np.random.rand(1)[0])

print(f"Os números sorteados para a mega sena foram: {lista_ordenada}.")
print(f"A probabilidade de vitória é de: {probabilidade}")