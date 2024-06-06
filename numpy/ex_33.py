import numpy as np

dias = int(input("Quantidade de dias: "))

vetor = np.random.uniform(-1, 1, dias)
vetor_positivo = vetor[vetor > 0]

print(f"Retornos: {vetor}") 
print(f"Retornos positivos: {vetor_positivo}")
print(f"Primeiro retorno: {vetor[0]}")
print(f"Último retorno: {vetor[-1]}")
