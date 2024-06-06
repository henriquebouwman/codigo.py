empresa = input("Qual o ticker da empresa? ")
cotacao = float(input("Digite a cotação? "))

print(f"A empresa {empresa} caso suba 100% terá o valor de {cotacao + cotacao * 1}")
print(f"A empresa {empresa} caso caiu 50% terá o valor de {cotacao - cotacao * 0.5}")