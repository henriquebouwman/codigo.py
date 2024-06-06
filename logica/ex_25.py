lista = [2, 4, 5, 6, 10]

lista_acima_de_5 = [numero for numero in lista if numero > 5]
lista_acima_de_5 = list(filter(lambda x: x > 5, lista))

print(lista_acima_de_5) 