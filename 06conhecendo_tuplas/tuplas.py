frutas = ("Laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

## Acesso direto aos valores da tupla

frutas = ("Laranja", "pera", "uva", "pera",)
print(frutas[0])
print(frutas[2])

## indices negativos 

frutas = ("Laranja", "pera", "uva", "pera",)
print(frutas[-1])
print(frutas[-3])

# Tuplas aninhadas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
matriz[0] # [1, 'a', 2]
matriz[0][0] # 1
matriz[1][-1] # 2 
matriz[-1][-1] # c

## FATIAMENTO 

tupla = ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[:3]) # ('p', 'y', 't')
print(tupla[3:]) # ('h', 'o', 'n')
print(tupla[1:3]) # ('y', 't')  
print(tupla[-4:-1]) # ('h', 'o')    
print(tupla[::])  # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) # ('n', 'o', 'h', 't', 'y', 'p')