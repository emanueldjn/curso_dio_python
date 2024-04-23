from datetime import datetime 

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"

# Tirar do horario americano
mascara_ptbr =  "%d/%m/%Y %a"
print(data_hora_atual.strftime(mascara_ptbr))

# Quando quero fazer uma conversão:
mascara_en = "%Y-%m-%d %H:%M"
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))