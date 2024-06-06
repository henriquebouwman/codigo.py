import re

expressao_regular = r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$'

while True:
	telefone = input("Digite seu telefone: ")
	if re.fullmatch(expressao_regular, telefone):
		print("Telefone válido!")
		break
	else:
		print("Telefone inválido! Digite novamente")
