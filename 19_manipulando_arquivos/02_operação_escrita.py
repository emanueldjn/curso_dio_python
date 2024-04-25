# Manipulação de escrita com python

arquivo = open('19_manipulando_arquivos/teste.txt', 'w')
# escrevendo no arquivo

arquivo.write("Escrevendo dados no novo arquivo.")
arquivo.writelines(["Escrevendo ", "um ", "novo ", "texto "])
arquivo.writelines(["\n", "Escrevendo ", "\n", "um ", "\n", "novo ", "\n", "texto "])
arquivo.close()