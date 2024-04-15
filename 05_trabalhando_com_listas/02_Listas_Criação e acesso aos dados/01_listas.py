frutas = ["laranja", "limao", "abacate", "maçã"]
print(frutas[2])

frutas = ["laranja", "limao", "abacate", "maçã"]
print(frutas[-1])

frutas = []
print(frutas)

letras = list("python") ## onde cada letra é um elemento da lista
print(letras)

numeros = list(range(10))   # gera uma lista com os numeros de 0 a 9
print(numeros)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True] 
print(carro)


## Listas dentro de listas 

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
matriz[0] # [1, 'a', 2]
matriz[0][0] # 1
matriz[1][-1] # 2 
matriz[-1][-1] # c

print("----------------------------------")

## Função enumerate 

carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("----------------------------------")

## Filtro versão 1 

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros: 
    if numero % 2 == 0:
        pares.append(numero)

print("----------------------------------")

# Versão 2 do filtro 

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]


print("----------------------------------")

## Modificando valores versão 1 

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros: 
    quadrado.append(numero ** 2)

print("----------------------------------")

## Modificando valores versão 2

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
