lista_cotacoes = []
contador = 0
while True:
	contador += 1
	cotacao = float(input(f"Digite a cotação do {contador} dia: "))
	lista_cotacoes.append(cotacao)
	continuar = input("Deseja continuar? [S/N]").upper()
	if continuar != "S" and continuar != "N":
		invalido = True
		while invalido:
			continuar = input("Digite um valor válido? [S/N]").upper()
			if continuar == "S" or continuar == "N":
				invalido = False
	if continuar == "N":
		break

if len(lista_cotacoes) < 2:
	print("Não é possivel calcular o retorno diário com apenas uma cotação.")

def calcular_retornos(lista):
	dicionario_retornos = {}
	for i in range(1,len(lista)):
		retorno = lista[i]/lista[i - 1] - 1
		retorno_percentual = "{:.2%}".format(retorno)
		dicionario_retornos[f"Retorno dia {i}"] = retorno_percentual
	return dicionario_retornos

print(calcular_retornos(lista_cotacoes))


