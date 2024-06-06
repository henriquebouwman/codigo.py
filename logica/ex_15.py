petrobras = {
	"Nome": "Petrobras",
	"CNPJ": "1201200120001",
	"Ticker": "PETR4",
	"Ano fundação": 1980,
	"Segmento": "Novo Mercado",
	"P/L": 20,
	"ROE": 0.20
}

print(f"Nome: {petrobras['Nome']}\n")
print(f"CNPJ: {petrobras['CNPJ']}\n")
print(f"Ticker: {petrobras['Ticker']}\n")
print(f"Ano fundação: {petrobras['Ano fundação']}\n")
print(f"Segmento: {petrobras['Segmento']}\n")
print(f"P/L: {petrobras['P/L']}\n")
print(f"ROE: {petrobras['ROE']}\n")

compraria = input("Você compraria? [S/N]")
if compraria == "S":
	compraria = "Compra"
if compraria == "N":
	compraria = "Não compra"

petrobras["Decisão de compra:"] = compraria

print(petrobras)

