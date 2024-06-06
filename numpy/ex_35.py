import numpy as np

contador = 0
rentabilidades = np.array([])

while True:
	contador += 1
	rentabilidade = float(input(f"Digite a rentabilidade da ação {contador}: "))
	rentabilidades = np.append(rentabilidades, rentabilidade)

	continuar = input("Você quer continuar? [S/N]").upper()
	if continuar != "S" and continuar != "N":
		invalido = True
		while invalido:
			continuar = input("Digito inválido. Você quer continuar? [S/N]").upper()
			if continuar == "S" or continuar == "N":
				invalido = False
	if continuar == "N":
		break		

def formatar_porcentagem(valor):
	return "{:.2%}".format(valor)

media = formatar_porcentagem(np.mean(rentabilidades))
desvio_p = formatar_porcentagem(np.std(rentabilidades))
mediana = formatar_porcentagem(np.median(rentabilidades))
maior = formatar_porcentagem(rentabilidades.max())
menor = formatar_porcentagem(rentabilidades.min())

print(f'''\nEstatisticas das rentabilidades:\n
Média: {media}
Mediana: {mediana}
Desvio padrão: {desvio_p}
Rentabilidade máxima: {maior}
Rentabilidade mínima: {menor}
	''')	