frutas = ["limão", "uva", "Laranja"]
curso = "curso de python"
print("Laranja" in frutas) #true
print("limão" not in frutas) ## false
print("python" in curso)   # True

print("------------------------------------------------")

curso = "Curso Python"
frutas = ["Laranja", "Uva", "Limão"]
saques = [1500, 100]

## saber se a str python esta presente na string curso
print("Python" in curso) ## True

## saber se a str maça esta presente na string frutas
print("Maçã" not in frutas)  ## True

## saber se teve um saque de 200
print(200 in saques)  ## false