# Para ler arquivos em Python

arquivo = open('19_manipulando_arquivos/anotações.md', 'r')
print(arquivo.read()) # todo conteúdo de uma vez só
print(arquivo.readline())   # Ir linha a linha sem carregar todo material 
print(arquivo.readlines()) # carregar todo conteudo do arquivo mas separando em uma lista para pré proessamento 

# Tip
# while len(linha  := arquivo.readline()):
#   print(linha)

arquivo.close()