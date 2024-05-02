-- Operação em Lote:
-- quando precisamos inserir muitos registro de uma vez. Pthon DB API, podemos usar o método 'executemany()' para isso.

data = [(5, 'abcde'), (6, abcdef), (7, abcdefg)]
cursor. executemany("INSERT INTO minha_tabela VALUES (?,?)", data)
con.commit()