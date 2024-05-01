# Visão geral dos tipos de dados NoSQL

# Tipos 
1. Key-Value: Chave-valor:
    --> Armazena dados como pares de chave e valor, onde cada chave é um identificador único para aessar o valor correspondente
    ex de SGBD: Redis, Riak, Amazon DynamoDB
    USO: um site pode usar um banco de dados Redis para armazenar informações de sessão de um usuário

2. Documento:
    Armazenam dados em documentos semiestruturados, eralmente em formato JSON ou BSON. 
    ex de SGBD: MongoDB, Couchbase, Apache CouchDB
    USO: um catálogo de ecommerce pode usar o MongoDB para armazenar informações de produtos, como nome, descrição, preço e att adicionais.

3. Coluna:
    Armezenam dados em formato de colunas. Permite alta escalabilidade e eficiência em determinados tipos de consultas.
    ex de SGBD:  Apache Cassandra, ScyllaDB, HBase
    USO: Um sistema de registro de aplicativos pode usar o apache cassandra para armazenar registro e log.

4. Grafos:
    Armazena e consulta dados interconectados, onde os relacionamentos entre os dados são tão importantes quanto os própriosdados.
    ex de SGBD: Neo4j, Amazon Neptune, JanusGraph
    USO: Uma rese social pode usar o Neo4j para armazenar os perfis dos usuários e suas conexões, permitindo consultas eficientes para encontrar amigos em comum.



