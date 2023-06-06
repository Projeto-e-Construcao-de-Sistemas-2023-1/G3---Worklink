CREATE DATABASE db_worklink;
USE db_worklink;

CREATE TABLE DESENVOLVEDOR (
		cod_desenvolvedor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(20) NOT NULL,
		sobrenome VARCHAR(30) NOT NULL,
		CPF CHAR(11) NOT NULL,
		email VARCHAR(50) NOT NULL,
		genero VARCHAR(12) NOT NULL,
		data_nascimento DATE NOT NULL,
        telefone VARCHAR(14) NOT NULL,
		conta_bancaria VARCHAR(11) NOT NULL,
		senha VARCHAR(50) NOT NULL,
		descricao VARCHAR(300),
		status_desenvolvedor BIT(1),
		tag_desenvolvedor VARCHAR(30) 

);

CREATE TABLE EMPRESA (
		cod_empresa INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        CNPJ CHAR(18) NOT NULL,
		razao_social VARCHAR(20) NOT NULL,
        email VARCHAR(50) NOT NULL,
        telefone VARCHAR(14) NOT NULL,
		conta_bancaria VARCHAR(11) NOT NULL,
		senha VARCHAR(50) NOT NULL,
		area_negocio VARCHAR(20) NOT NULL
);

CREATE TABLE CARTEIRA_DESENVOLVEDOR (
		id_carteira_dev INT AUTO_INCREMENT PRIMARY KEY,
		saldo DECIMAL(10, 2),
        cod_desenvolvedor INT,
		FOREIGN KEY (cod_desenvolvedor) REFERENCES DESENVOLVEDOR(cod_desenvolvedor)
);

CREATE TABLE CARTEIRA_EMPRESA (
		id_carteira_emp INT AUTO_INCREMENT PRIMARY KEY,
        saldo DECIMAL(10, 2),
		cod_empresa INT,
		FOREIGN KEY (cod_empresa) REFERENCES EMPRESA(cod_empresa)
);

CREATE TABLE PROJETO (
		cod_projeto INT AUTO_INCREMENT PRIMARY KEY,
		cod_empresa INT,
		FOREIGN KEY (cod_usuario) REFERENCES EMPRESA(cod_empresa),
		especificacao VARCHAR(50) NOT NULL,
		valor_orcamento DECIMAL(10, 2) NOT NULL,
		prazo DATE,
		requisito_tecnico VARCHAR(50) NOT NULL,
		status_projeto VARCHAR(50) NOT NULL,
		tag_projeto VARCHAR(30) NOT NULL
);

CREATE TABLE DESENVOLVEDOR_PROJETO (
		cod_desenvolvedor_projeto INT AUTO_INCREMENT PRIMARY KEY,
		cod_desenvolvedor INT,
		FOREIGN KEY (cod_desenvolvedor) REFERENCES DESENVOLVEDOR(cod_desenvolvedor),
		cod_projeto INT,
		FOREIGN KEY (cod_projeto) REFERENCES PROJETO(cod_projeto)
);

CREATE TABLE DESENVOLVEDOR_EMPRESA (
		cod_desenvolvedor_empresa INT AUTO_INCREMENT PRIMARY KEY,
		cod_desenvolvedor INT,
		FOREIGN KEY (cod_desenvolvedor) REFERENCES DESENVOLVEDOR(cod_desenvolvedor),
		cod_empresa INT,
		FOREIGN KEY (cod_empresa) REFERENCES PROJETO(cod_empresa)
);  