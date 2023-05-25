
CREATE TABLE carteira_digital (
                cod_carteira VARCHAR(20) NOT NULL,
                saldo DOUBLE PRECISION,
                PRIMARY KEY (cod_carteira)
);


CREATE TABLE Tb_USUARIO (
                cod_usuario VARCHAR(20) NOT NULL,
                telefone VARCHAR(14) NOT NULL,
                email VARCHAR(50) NOT NULL,
                conta_bancaria VARCHAR(11) NOT NULL,
                senha VARCHAR(50) NOT NULL,
                PRIMARY KEY (cod_usuario)
);


CREATE TABLE DESENVOLVEDOR (
                cod_usuario VARCHAR(20) NOT NULL,
                CPF CHAR(11) NOT NULL,
                nome VARCHAR(20) NOT NULL,
                sobrenome VARCHAR(30) NOT NULL,
                genero VARCHAR(12) NOT NULL,
                data_nascimento DATE NOT NULL,
                habilidade VARCHAR(50) NOT NULL,
                experiencia VARCHAR(300),
                status_desenvolvedor BIT(1) NOT NULL,
                tag_desenvolvedor VARCHAR(30) NOT NULL,
                PRIMARY KEY (cod_usuario)
);


CREATE TABLE carteira_desenvolvedor (
                cod_usuario VARCHAR(20) NOT NULL,
                cod_carteira VARCHAR(20) NOT NULL,
                PRIMARY KEY (cod_usuario, cod_carteira)
);


CREATE TABLE EMPRESA (
                cod_empresa VARCHAR(20) NOT NULL,
                cod_usuario VARCHAR(20) NOT NULL,
                CNPJ CHAR(18) NOT NULL,
                razao_social VARCHAR(20) NOT NULL,
                area_negocio VARCHAR(20) NOT NULL,
                PRIMARY KEY (cod_empresa, cod_usuario)
);


CREATE TABLE carteira_empresa (
                cod_empresa VARCHAR(20) NOT NULL,
                cod_usuario VARCHAR(20) NOT NULL,
                cod_carteira VARCHAR(20) NOT NULL,
                PRIMARY KEY (cod_empresa, cod_usuario, cod_carteira)
);


CREATE TABLE PROJETO (
                cod_projeto VARCHAR(20) NOT NULL,
                cod_empresa VARCHAR(20) NOT NULL,
                cod_usuario VARCHAR(20) NOT NULL,
                especificacao VARCHAR(50) NOT NULL,
                valor_orcamento DOUBLE PRECISION NOT NULL,
                prazo DATE NOT NULL,
                requisito_tecnico VARCHAR(50) NOT NULL,
                status_projeto VARCHAR(50) NOT NULL,
                tag_projeto VARCHAR(30) NOT NULL,
                PRIMARY KEY (cod_projeto, cod_empresa, cod_usuario)
);


ALTER TABLE carteira_empresa ADD CONSTRAINT carteira_digital_carteira_empresa_fk
FOREIGN KEY (cod_carteira)
REFERENCES carteira_digital (cod_carteira)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE carteira_desenvolvedor ADD CONSTRAINT carteira_digital_carteira_desenvolvedor_fk
FOREIGN KEY (cod_carteira)
REFERENCES carteira_digital (cod_carteira)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE EMPRESA ADD CONSTRAINT tb_usuario_empresa_fk
FOREIGN KEY (cod_usuario)
REFERENCES Tb_USUARIO (cod_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE DESENVOLVEDOR ADD CONSTRAINT tb_usuario_desenvolvedor_fk
FOREIGN KEY (cod_usuario)
REFERENCES Tb_USUARIO (cod_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE carteira_desenvolvedor ADD CONSTRAINT desenvolvedor_carteira_desenvolvedor_fk
FOREIGN KEY (cod_usuario)
REFERENCES DESENVOLVEDOR (cod_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE PROJETO ADD CONSTRAINT empresa_projeto_fk
FOREIGN KEY (cod_usuario, cod_empresa)
REFERENCES EMPRESA (cod_usuario, cod_empresa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE carteira_empresa ADD CONSTRAINT empresa_carteira_empresa_fk
FOREIGN KEY (cod_usuario, cod_empresa)
REFERENCES EMPRESA (cod_usuario, cod_empresa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;