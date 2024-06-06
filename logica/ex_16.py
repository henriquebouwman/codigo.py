empresa = input("Digite o nome da empresa: ")
primeira_letra = empresa[0]
ultima_letra = empresa[-1]
qtd_letras = len(empresa)
nome_maiusculo = empresa.upper()
nome_pri_maiuscula = empresa.title()
tranqueira = empresa.replace(empresa[0:2], "Tranqueira")
print(f"Primeira letra: {primeira_letra}")
print(f"Última letra: {ultima_letra}")
print(f"Tamanho da palavra: {qtd_letras} caracteres")
print(f"Nome maiúsculo: {nome_maiusculo}")
print(f"Primeira maiúscula: {nome_pri_maiuscula}")
print(f"Tranqueira: {tranqueira}")