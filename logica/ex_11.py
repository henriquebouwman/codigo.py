import random

lista = []
for i in range(4):
	empresa = input("Digite o ticker de uma empresa: ")
	lista.append(empresa)

empresa_escolhida = random.choice(lista)

print(f"É recomendado a compra da empresa {empresa_escolhida}")