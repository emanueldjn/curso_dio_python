# Tabelas
Usada para armazenar dados de forma organizada. ada Tabela em um banco de dados relacional temum nome unico
e é dividida em colunas e linhas 

# Coluna 
para tributo especifico
cada coluna tem nome unico e tipo de dado associado que define o tipo de informação que pode ser armazenado
como numero, textos, datas etc...

# Registro
Conhecido como linha ou tupla. É umainstancia individual de dados em uma tabela 

# Comando: CREATE TABLE

CREATE TABLE {{nome}}
    ({{coluna}} {{tipo}} {{opções}} COMMENT
{{'COMENTARIO}});

# Tipos de dados:
inteiro (integer)
Decimal/Numerico (Decimal/Numeric)
Caractere/Varchar(Character/Varchar)
Data/Hora(Date/Time)
Booleano(Boolean)
Texto longo(Text)

# Comando: CREATE TABLE - OPÇÕES
Restrições de valor:
    NOT NULL - não aceita nulo
    UNIQUE - nao ter mais de um usuario igual 
    DEFAULT
Chaves primarias e estrangeiras
auto incremento