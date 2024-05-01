# Estrutura do MongoDB
data base - documento - coleções 

# Coleções 
--> Agrupamento logico de documentos
--> Não exige esquema ou que os documentos tenham a mesma estrutura 

# Caracterisicas
1. Os nomes das coleções tem que seguir algumas regras:
    - Começar com uma letra ou um underscore(_);
    - Podem conter letrar, números ou underscores.
    - Não podem ser vazios.
    - Não podem ter mais de 64bytes de comprimento.

# Documentos 
--> são armazenados em documentos BSON(Binary JSON), que são estruturas flexiveis e semiestruturadas.
--> Cada documento possui um identificador unico chamado "_id"
--> Composto por pares de chaves e valores 

# Tipos de dados simples
1. String
2. Number
3. Boolean
4. Date
5. Null
6. Objectld

# Tipos de dados complexos
1. Arrays
2. Documento embutido (Embedded Document)
3. Referência (Reference)
4. GeoJSON

# Estrutura de um documento

{ 
    _id:Objectld(""),
    "nome_campo":"valor_campo",
    ...
}

# Formatted JSON Data
{
   "_id":1,
   "nome":"Emanuel Nascimento",
   "idade":23,
   "data_nascimento":"2000-29-05",
   "endereco":"Buenos Aires",
   "enderecos":{
      "logradouro":"Rua pedro f..",
      "numero":123,
      "bairro":"centro",
      "cidade":"CB"
   }
}

# Array

{
   "_id":1,
   "nome":"Emanuel Nascimento",
   "idade":23,
   "data_nascimento":"2000-29-05",
   "endereco":"Buenos Aires",
   "enderecos":[
      {
         "logradouro":"Rua pedro f..",
         "numero":123,
         "bairro":"centro",
         "cidade":"CB"
      }
   ]
}