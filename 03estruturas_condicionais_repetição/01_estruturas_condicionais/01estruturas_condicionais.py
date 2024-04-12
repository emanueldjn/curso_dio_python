MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aula teoria, mas não pode fazer aulas praticas.")

else: 
    print("Menor de idade, não pode tirar a CNH!")
