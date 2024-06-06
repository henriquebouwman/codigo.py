from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

data_digitada = str(input("Digite uma data no formato brasileiro (dd/mm/yyyy): "))

data = datetime.strptime(data_digitada,"%d/%m/%Y").date()
dia_anterior = data - timedelta(days = 1)
ano_seguinte = data + relativedelta(years = 1)

print(f"A data digitada foi {data}")
print(f"O dia anterior a data é {dia_anterior}")
print(f"O ano seguinte a data é {ano_seguinte}")