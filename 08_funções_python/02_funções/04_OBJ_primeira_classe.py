# Ex

def somar(a, b):
    return a + b 

def  subtrair(a, b):
    return a - b

def test(a, b):
    return a*2 + b*3

def exibir_resultado(a, b, funcao):
    # Recebe a b e função; funçao: função executa a função(a, b) e passa os argumentos para ele
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

# Chamada da função 
exibir_resultado(10, 10, somar) #  Resultado 10 + 10 = 20 
exibir_resultado(10, 5, subtrair) # resultado 10 - 5 = 5
exibir_resultado(10, 10, test) # resultado = 50

# Objetos de primeira classe

op = somar
print(op(1, 25)) # O resultado é o mesmo que somar 1 + 23 