valor = float(input("Digite os graus celsius: "))

def transformar(celsius):
	fahrenheit = (celsius  * 9/5) + 32
	return fahrenheit

print(f"{valor} graus celsius = {transformar(valor)} fahrenheit.")
