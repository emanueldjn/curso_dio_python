# Objetivo Geral
--> Abordar os conceitos basicos de banco de dados e como podemos interagir com eles usando a DB API em Python


# O que é um banco de dados?
Os bancos de dados são oleções organizadas de dados, geralmente armazenados e acessados eletronicamente a partir deum sistema de computador.

# Tipos:
1. Relacionais
2. Nao relacionais
3. Orientado a objetos 

O mais comum é o Relacional que organiza os dados em tabelas.
Cada tabela é composta de linhas que representam registros individuais e colunas que representam campos de dados.

--> Cada linha representa um registro distinto e cada coluna representa um tipo de informação, chamado de campo.
Por exemplo uma tabela 'Clientes' pode ter campos como 'id', 'nome', 'email' e 'telefone'.
--> cada tabela deve ter uma chave primaria 
--> Chave primaria é uma coluna (ou conjunto de colunas) cujo valor é unico para cada registro. isso garante que cada registro na tabela possa ser identificado de maneira única. 
ex: 
'clientes' o campo 'id' pode ser a chave primaria 

# Papel de Um SGBD - Sistema de Gerenciamento de Banco de Dados:
são softwares que interagem com o usuário, outras aplicações e o próprio banco de dados para capturar e analisar os dados.
--> MySQL, PostgreSQL, SQLite, Oracle, Database, Microsoft SQL Server e MariaDB

# Chaves estrangeiras 
--> Com as chaves estrangeiras que relacionamos um dado com outro dado.

em uma tabela 'pedidos', podemos ter um campo 'ClienteID' que seja uma chave estrangeira apontando para chave primária da tabela 'clientes'. Isso cria um relacionamento entre 'pedidos' e clientes', permitindo que cada pedido seja associado a um cliente especifico.

# Relacionamento entre tabelas
As relacoes podem ser:
um para um
um para muitos 
muitos para muitos

--> Permitem efetuar consultas complexas que unem dados de várias tabelas

# SQL:

Linguagem usada para interagir com bancos de dados relacionais. Com SQL, podemos criar tabelas, inserir, atualizar e delear registros
bem como executar consultas para buscar dados.

exemplo de codigo:
[text](01_ex_codigo.sql)

# Conectando a un Banco de Dados
Estabelecer uma conexão. Fazemos isso usando o Python DB API

exemplo de codigo: 
import sqlite3
con = sqlite3.connect('meu_banco_de_dados.db')

# Operação em Lote:
quando precisamos inserir muitos registro de uma vez. Pthon DB API, podemos usar o método 'executemany()' para isso.

ex: 
[text](02_ex_codigo.sql)