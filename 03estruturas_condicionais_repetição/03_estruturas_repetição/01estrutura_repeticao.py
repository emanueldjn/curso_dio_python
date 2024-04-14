texto = input("informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
  
print() #add uma quebra de linha
    