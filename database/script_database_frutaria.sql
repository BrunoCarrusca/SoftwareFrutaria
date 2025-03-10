-- Active: 1729008556189@@127.0.0.1@3306@frutaria
CREATE DATABASE frutaria;

USE frutaria;

-- Tabela de Fornecedores
CREATE TABLE fornecedor(
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome_fornecedor VARCHAR(250) NOT NULL,
    num_telemovel_fornecedor VARCHAR(13) NOT NULL,
    endereco_fornecedor VARCHAR(500) NOT NULL,
    email_fornecedor VARCHAR(40) UNIQUE NOT NULL
);

-- Tabela de Administradores
CREATE TABLE administrador(
    id_administrador INT PRIMARY KEY AUTO_INCREMENT,
    nome_administrador VARCHAR(250) NOT NULL,
    num_telemovel_administrador VARCHAR(13) NOT NULL,
    endereco_administrador VARCHAR(500) NOT NULL,
    email_administrador VARCHAR(40) UNIQUE NOT NULL
);

-- Tabela de Clientes
CREATE TABLE cliente(
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(250) NOT NULL,
    num_telemovel_cliente VARCHAR(13) NOT NULL,
    endereco_cliente VARCHAR(500) NOT NULL,
    email_cliente VARCHAR(40) UNIQUE NOT NULL
);

-- Tabela de Funcionários
CREATE TABLE funcionario(
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome_funcionario VARCHAR(250) NOT NULL,
    num_telemovel_funcionario VARCHAR(13) NOT NULL,
    endereco_funcionario VARCHAR(500) NOT NULL,
    email_funcionario VARCHAR(40) UNIQUE NOT NULL
);

-- Tabela de Artigos
CREATE TABLE artigo(
    id_artigo INT PRIMARY KEY AUTO_INCREMENT,
    nome_artigo VARCHAR(250) NOT NULL,
    quantidade_artigo DECIMAL(5, 3) NOT NULL,
    preco_artigo DECIMAL(5, 2) NOT NULL,
    id_fornecedor INT REFERENCES fornecedor(id_fornecedor) 
);

-- Tabela de Vendas ao Cliente
CREATE TABLE venda_cliente (
    id_venda_cliente INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    id_artigo INT,
    id_funcionario INT,
    quantidade_venda_cliente INT NOT NULL,
    preco_venda_cliente DECIMAL(10,2) NOT NULL,
    preco_total_venda_cliente DECIMAL(10,2) NOT NULL,
    data_venda_cliente DATE NOT NULL,
    hora_venda_cliente TIME NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_artigo) REFERENCES artigo(id_artigo),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
);

-- Tabela de Compras do Fornecedor
CREATE TABLE compra_fornecedor (
    id_compra_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    id_artigo INT,
    id_administrador INT,
    id_fornecedor INT,
    quantidade_compra_fornecedor INT NOT NULL,
    preco_compra_fornecedor DECIMAL(10,2) NOT NULL,
    preco_total_compra_fornecedor DECIMAL(10,2) NOT NULL,
    data_compra_fornecedor DATE NOT NULL,
    hora_compra_fornecedor TIME NOT NULL,
    FOREIGN KEY (id_artigo) REFERENCES artigo(id_artigo),
    FOREIGN KEY (id_administrador) REFERENCES administrador(id_administrador),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor)
);