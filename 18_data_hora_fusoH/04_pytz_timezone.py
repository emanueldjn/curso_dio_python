# Exemplo de codigo, TimeZone Fuso horario:
# pip install pytz - terminal 

import pytz 
from datetime import  datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print('-----------------------------------------------------------------')
print(f"Data e hora atual (Fuso Horário Europe/Oslo): {data}")
print('-----------------------------------------------------------------')
print(f"Data e hora atual (Fuso Horário America/Sao_Paulo): {data2}")