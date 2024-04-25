# Exemplo

import os
import shutil 
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criando um diretorio
os.mkdir(ROOT_PATH / "novo_diretorio")
arquivo = open(ROOT_PATH / "novo.txt",'w')
arquivo.close()

# Renomeando um arquivo
os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / "alterado.txt")

# Remover um arquivo
os.remove(ROOT_PATH / "alterado.txt")

# Mover um arquivo
shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / "novo_diretorio" / "novo.txt")