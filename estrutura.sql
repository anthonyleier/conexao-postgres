CREATE DATABASE sistema;

DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO usuario (nome, email, senha) VALUES
('Eduarda Azevedo', 'eduarda.azevedo@gmail.com', 'eduarda123'),
('Bianca Araújo', 'bianca.araujo@gmail.com', 'bianca123'),
('Lucas Carvalho', 'lucas.carvalho@gmail.com', 'lucas123'),
('Rafaela Barros', 'rafaela.barros@gmail.com', 'rafaela123'),
('João Martins', 'joao.martins@gmail.com', 'joao123'),
('Gabriel Costa', 'gabriel.costa@gmail.com', 'gabriel123'),
('Isabelle Fernandes', 'isabelle.fernandes@gmail.com', 'isabelle123'),
('José Rocha', 'jose.rocha@gmail.com', 'jose123'),
('Vinicius Gomes', 'vinicius.gomes@gmail.com', 'vinicius123'),
('Victor Oliveira', 'victor.oliveira@gmail.com', 'victor123'),
('Mariana Melo', 'mariana.melo@hotmail.com', 'mariana123'),
('Lara Costa', 'lara.costa@hotmail.com', 'lara123'),
('Gustavo Dias', 'gustavo.dias@hotmail.com', 'gustavo123'),
('Gabrielly Fernandes', 'gabrielly.fernandes@hotmail.com', 'gabrielly123'),
('Matilde Oliveira', 'matilde.oliveira@hotmail.com', 'matilde123'),
('Lívia Carvalho', 'livia.carvalho@hotmail.com', 'livia123'),
('Tânia Castro', 'tania.castro@hotmail.com', 'tania123'),
('Victoria Alves', 'victoria.alves@hotmail.com', 'victoria123'),
('Bruno Gonçalves', 'bruno.goncalves@hotmail.com', 'bruno123'),
('Erick Gonçalves', 'erick.goncalves@hotmail.com', 'erick123');