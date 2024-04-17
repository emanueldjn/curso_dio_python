def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # 64
print(retornar_antecessor_e_sucessor(10)) # (9, 11) retornou uma tupla = imutavel 

print("--------------------------------------")

def func_3():
    print("Hello World")
    # return none 

print(func_3()) # Hello World