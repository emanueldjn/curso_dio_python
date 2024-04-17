# Exemplo

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-123") # Sequencial OBS: Posse passar o valor trocado e ficar errado

# Conjunto chave=valor OBS: não há como passar valor errado. Porém podem modificar o nome do argumento e dar errado. 
salvar_carro(marca="Fiat", modelo="Uno", ano=2005, placa="ABC-1234") 

# Passando para um dicionario para a função: *args e **kwargs 
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

#carro inserido com sucesso! Fiat/palio/1999/ABC-1234