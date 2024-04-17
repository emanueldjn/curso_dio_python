# Passando uma data que o poema foi criado, lista de versos, informações do poema.

def exibir_poema(data_extenso, *lista, **dicionario): #args e kwargs
    texto = "\n".join(lista) # concatenando com \n um em cada linha
    
    # Recebo o kwars .items porque é dicionario. entregar uma lista de tuplas com chave=valor; vai iterar;
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    
    # Criando variavel mensagem -- 2 quebras de linha -- data por extenso -- 
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# Testetando função 
exibir_poema("Terça-Feira, 16 de março de 2024", "Zen of Python", "Beautiful is better than ugly." "Explicit is better than implicit", autor="Tim Peters", ano=1999)

# Tupla = valores separados por virgulas dentro de um ()