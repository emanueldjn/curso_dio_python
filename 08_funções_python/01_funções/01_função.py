# Exemplo declarando função 

def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem_2(nome): # nome = argumento
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}")

# Executando função
exibir_mensagem()
exibir_mensagem_2(nome="Emanuel")
exibir_mensagem_2("Fulano")
exibir_mensagem_3()
exibir_mensagem_3(nome="Esteffany")