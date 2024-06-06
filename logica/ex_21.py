lista_nome = []
lista_pl = []
lista_roe = []

menor_pl = 1000000000000

while True:
	nome = input("Digite o nome da empresa: ").title()
	pl = int(input(f"Digite o P/L da {nome}: "))
	roe = float(input(f"Digite o ROE da {nome}: "))
	
	lista_nome.append(nome)
	lista_pl.append(pl)
	lista_roe.append(roe)

	if menor_pl > pl:
		menor_pl = pl
		nome_menorpl = nome

	continuar = input("Desejar inserir dados de outra empresa? [S/N]").upper()
	if continuar != "S" and continuar != "N":
		invalido = True
		while invalido:
			continuar = input("Digite um valor válido: [S/N]").upper()
			if continuar == "S" or continuar == "N":
				invalido = False
	if continuar == "N":
		break

numero_ativos = len(lista_nome)
media_pl = sum(lista_pl)/len(lista_pl)
media_roe = sum(lista_roe)/len(lista_roe)
media_roe = "{:.0%}".format(media_roe)

print(f"Existem {numero_ativos} ativos na carteira.")
print(f"A média de P/L da carteira é {media_pl}.")
print(f"A média do ROE da carteira é {media_roe}.")
print(f"A empresa mais barata da carteira é {nome_menorpl} com {menor_pl} de P/L.")
if len(lista_nome) < 3:
	print(f"Sua carteira está muito concentrada em poucos ativos!")
