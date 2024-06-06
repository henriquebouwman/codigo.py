import numpy as np

empresas = np.array(["Petrobras", "Vale", "Weg"])
lucros = np.array([])

for empresa in empresas:
	lucro = float(input(f"Digite o lucro da {empresa}: "))
	lucros = np.append(lucros, lucro)

lucros = -np.sort(-lucros)

print(f"O lucro das empresas, do maiso pra o menor: {lucros}")