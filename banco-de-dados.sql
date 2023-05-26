
CREATE TABLE USUARIO (
                cod_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                telefone VARCHAR(14) NOT NULL,
                email VARCHAR(50) NOT NULL,
                conta_bancaria VARCHAR(11) NOT NULL,
                senha VARCHAR(50) NOT NULL
                
);


CREATE TABLE DESENVOLVEDOR (
				cod_usuario INT,
				FOREIGN KEY (cod_usuario) REFERENCES USUARIO(cod_usuario),
                CPF CHAR(11) NOT NULL,
                nome VARCHAR(20) NOT NULL,
                sobrenome VARCHAR(30) NOT NULL,
                genero VARCHAR(12) NOT NULL,
                data_nascimento DATE NOT NULL,
                habilidade VARCHAR(50) NOT NULL,
                experiencia VARCHAR(300),
                status_desenvolvedor BIT(1),
                tag_desenvolvedor VARCHAR(30) 
                
);

CREATE TABLE EMPRESA (
                cod_usuario INT,
				FOREIGN KEY (cod_usuario) REFERENCES USUARIO(cod_usuario),
                CNPJ CHAR(18) NOT NULL,
                razao_social VARCHAR(20) NOT NULL,
                area_negocio VARCHAR(20) NOT NULL
);


CREATE TABLE CARTEIRA_DIGITAL (
                cod_carteira INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                cod_usuario INT,
				saldo DECIMAL(10, 2),
				FOREIGN KEY (cod_usuario) REFERENCES USUARIO(cod_usuario)
                
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
                cod_usuario INT,
				FOREIGN KEY (cod_usuario) REFERENCES USUARIO(cod_usuario),
                especificacao VARCHAR(50) NOT NULL,
                valor_orcamento DECIMAL(10, 2) NOT NULL,
                prazo DATE,
                requisito_tecnico VARCHAR(50) NOT NULL,
                status_projeto VARCHAR(50) NOT NULL,
                tag_projeto VARCHAR(30) NOT NULL
);
carteira_desenvolvedor