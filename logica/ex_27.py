lista = ["WEGE3", "PETR4", "PETR3", "PCAR3", "ALPA4"]

lista_filtrada = [ticker for ticker in lista if ticker.startswith("P")]
lista_filtrada = [ticker for ticker in lista if ticker[0] == ("P")]

print(lista_filtrada)