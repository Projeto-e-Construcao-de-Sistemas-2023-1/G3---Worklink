CREATE TABLE DESENVOLVEDOR (
		telefone VARCHAR(14) NOT NULL,
                email VARCHAR(50) NOT NULL,
                conta_bancaria VARCHAR(11) NOT NULL,
                senha VARCHAR(50) NOT NULL,
                CPF CHAR(11),
                nome VARCHAR(20),
                sobrenome VARCHAR(30),
                genero VARCHAR(12),
                data_nascimento VARCHAR(20),
                habilidade VARCHAR(50),
                experiencia VARCHAR(300),
                status_desenvolvedor BIT(1),
                tag_desenvolvedor VARCHAR(30) 
                
);

CREATE TABLE EMPRESA (
		telefone VARCHAR(14) NOT NULL,
                email VARCHAR(50) NOT NULL,
                conta_bancaria VARCHAR(11) NOT NULL,
                senha VARCHAR(50) NOT NULL,
                CNPJ CHAR(18),
                razao_social VARCHAR(20),
                area_negocio VARCHAR(20)
);


CREATE TABLE CARTEIRA_DIGITAL (
                cod_carteira INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		saldo DECIMAL(10, 2)
				
);


CREATE TABLE CARTEIRA_DESENVOLVEDOR (
		id_carteira_dev INT AUTO_INCREMENT PRIMARY KEY,
                cod_carteira INT,
		FOREIGN KEY (cod_carteira) REFERENCES CARTEIRA_DIGITAL(cod_carteira)
);



CREATE TABLE CARTEIRA_EMPRESA (
		id_carteira_emp INT AUTO_INCREMENT PRIMARY KEY,
		cod_carteira INT,
		FOREIGN KEY (cod_carteira) REFERENCES CARTEIRA_DIGITAL(cod_carteira)
);


CREATE TABLE PROJETO (
                especificacao VARCHAR(50) NOT NULL,
                valor_orcamento DECIMAL(10, 2) NOT NULL,
                prazo DATE,
                requisito_tecnico VARCHAR(50) NOT NULL,
                status_projeto VARCHAR(50) NOT NULL,
                tag_projeto VARCHAR(30) NOT NULL
);
