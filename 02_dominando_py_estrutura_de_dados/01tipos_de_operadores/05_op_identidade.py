# Saber se o saldo ocupa a mesma regiao de memoria que limite

saldo = 1000
limite = 500

print(saldo is limite) #False / pois nao ocupa a mesma região de memoria
print(saldo is not limite) ## True / porque Realmente eles não ocupam a mesma região da memoria // # --> "e se ele nao é"

print("----------------")


saldo = 1000
limite = 1000

print(saldo is limite) #True / ocupa a mesma região de memoria
print(saldo is not limite) ## false / porque Realmente eles não ocupam a mesma região da memoria