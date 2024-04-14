## Dicionario 

pessoa = {"nome": "Emanuel", "Idade": 23}

pessoa = dict(nome= "Emanuel", idade=28)

## add uma nova chave ao dicionario. 
pessoa["telefone"] = "3333-1234" 
print(pessoa)

print('----------------------------------------')

## ACESSANDO DADOS DO DICIONARIO: 

dados = {"nome": "Emanuel", "idade": 23, "telefone": "3333-1234"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

print('----------------------------------------')


dados["nome"] = "maria"
print(dados["nome"])

dados["idade"] = 18
print(dados["nome"])

dados["telefone"] = "5555-0000"
print(dados["telefone"])


print('----------------------------------------')


## DICIONÁRIOS ANINHADOS 

contatos = {
    "1emanuelnas29@gmail.com": {"nome": "Emanuel", "telefone": "1111-1111"},
    "2emanuelnas29@gmail.com": {"nome": "Emanuel", "telefone": "2222-2222"},
    "3emanuelnas29@gmail.com": {"nome": "Emanuel", "telefone": "3333-3333"},
    "4emanuelnas29@gmail.com": {"nome": "Emanuel", "telefone": "4444-4444"},
}

contatos["1emanuelnas29@gmail.com"] ["telefone"] # 1111-1111

print('----------------------------------------')

## ITERAR DICIONARIO 

#for chave in contatos:
#    print(chave, contatos[chave])

for chave, valor in contatos.item():
    print(chave, valor)