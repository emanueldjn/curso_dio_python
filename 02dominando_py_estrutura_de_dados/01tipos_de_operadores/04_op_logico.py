## END = para ser True, tudo tem que ser True
## OR = para ser True, apenas um tem que ser True

print(True and True)  ## true
print(True and False) ## false
print(False and False) ##  false
print(True or True)    ## true
print(True or False)    ## true
print(False or False) ## false

saldo = 1000
saque = 250 
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque ## True
print(f"a expressao e: {exp}")

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) ## true
print(f"a expressao e: {exp_2} ")

## Melhor e mais facil separar em uma variavel, nomear ela e depois usar no codigo.

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)