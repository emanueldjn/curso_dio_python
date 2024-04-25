# O que são pacotes em python?
--> pacoes são modulos que podem ser instalados e utilizados em seus programas python. Eles permitem que você utilize código 
que foi escrito por outras pessoas, economizando tempo e esforço. 

--> o papel do pip:
    gerenciador de pacotes do python. Ele nos permite instalar, atualizar e remover pacotes. Ele se comunica com o Pypi(python package Index)
    que é onde a maioria dos pacotes são armazenados

https://pypi.org/

ex: criando um ecomerce e precisa disponibilizar pacotes via correio e precisa saber o cep com o valor do frete 
# como instalar um pacote com o pip

$ pip install nome_do_pacote
$ pip uninstall numpy
$ pip list


// ----------------------- // 

# Uso de Ambientes virtuais
Nos permitem manter as dependencias de diferentes projetos. isso é importante para evitar conflitos entre versões de pacotes

--> Para Criar ambiente virtual
python3 -m venv myenv   (venv é um módulo incorporado no Python)

--> para ativar o ambiente virtual
source myenv/bin/activate   (no windows use .\myenv\Scripts\activate)
deactivate                     (para sair do ambiente virtual)

# instalar um pacote
pip install nome_do_pacote

# Desistalar pacote
pip uninstall nome_do_pacote

# listar pacotes instalados
pip list

# atualizar um pacote
pip install --upgrade nome_do_pacote

//--------------------------------// 

# pipenv 
é uma ferramenta de gerenciamento de pacotes que combina gestão de dependencias com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

--> comandos:
pip install pipenv
pipenv ininstall numpy
pipenv uninstall numpy
pipenv graph
pipenv lock             # cria um arquivo Pipfile.lock

// ---------------------------------- // 

# poetry 
ferramenta de gerenciamento de dependencias que permite declarar as bibliotecas de que seu projeto depende de gerencia
(instala, atualiza, remove). Essas bibliotecas para voce. Suporta também empacotamento a publicação de projetos no PyPI.

--> comandos:
pip install poetry
poetry new myproject
cd myproject 
poetry add numpy
poetry remove numpy

// ------------------------- // 

# FERRAMENTAS DE CHECAGEM DE ESTILO 
# flake8
verificam nosso codigo e nos informam onde estamos desviando do guia de estilo (identação)

--> comandos:
pip install flake8
flake8 meu_script.py

# Formatação automatica de codigo: 
black é uma ferramenta que segue "formato unico"
reformata todo o arquivo em um estilo consistente, simplificando a tarefa de manter o codigo identado com a PEP 8

//-----------------------// 

ORGANIZAÇÃO DE IMPORTS COM ISORT
isort é uma ferramenta para classificar importações alfabeticamente e separa-las automaticamente em seções.

--> comandos:
pip install isort
isort meu_script.py