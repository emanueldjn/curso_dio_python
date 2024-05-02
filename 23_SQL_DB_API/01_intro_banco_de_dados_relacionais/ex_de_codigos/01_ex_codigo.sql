-- Cria um novo banco de dados
CREATE DATABASE loja;

-- Cria uma tabela para armazenar informações de produtos
CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), preco DECIMAL)

-- inclui um novo produto
INSERT INTO produtos (nome, preco) VALUES ('Curso de Python', 250.00);

-- Lista todos os produtos

SELECT * FROM produtos;

-- Atualiza o produto com id informado
UPDATE produtos SET nome='Curso de Python para iniciantes' WHERE id = 1;

-- Exlcui o produto com o id informado
DELETE FROM produtos WHERE id = 1;


-- Estabelecer uma conexão. Fazemos isso usando o Python DB API
