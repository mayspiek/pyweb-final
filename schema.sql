DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS produto;

CREATE TABLE cliente(
    -- chave primaria --
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome varchar(80) NOT NULL,
    cpf varchar(20),
    cep varchar(20),
    email varchar(80) NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- CREATE
INSERT INTO cliente (nome, cpf, cep, email)
VALUES
    ('admin', '1002000', '85850-100', 'admin@test.org'),
    ("Maria Silver", "949.282.111-82", '85850-900', "mariam@test.org"),
    ("Jairo Carlile", "144.217.577-11", '85850-400', "carlile@test.org"),
    ("Marcos Oliva", "433.144.644-52", '85850-200', "marcos@test.org");

CREATE TABLE produto(
    -- chave primaria --
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome varchar(120) NOT NULL,
    preco decimal(10,2),
    marca varchar(40),
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- CREATE
INSERT INTO produto (nome, preco, marca)
VALUES
    ('Ryzen 5700x', 102, 'AMD'),
    ('i9 13700k', 2210.91, 'Intel'),
    ('Samsung galaxy s30', 311, 'Samsung');
