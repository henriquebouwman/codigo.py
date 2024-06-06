try:
	nome = str(input("Digite seu nome: ")).title()
	idade = int(input("Digite sua idade: "))
	idade_3 = idade + 3

except Exception as erro:
	print(f"Houve um erro do tipo {erro.__class__}")

else:
	print(f"Oi {nome}, parabéns por estar participando do curso codigo.py!")
	print(f"Quando você tiver {idade_3} anos você será muito bom em Python.")