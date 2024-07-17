USE pfe_dev;

CREATE TABLE IF NOT EXISTS TipoProcedimento (
	id_tipo_proc INT PRIMARY KEY,
    nome VARCHAR(255)
);

INSERT INTO TipoProcedimento VALUES
    (0, "Simples"),
    (1, "Painel"),
    (2, "Painel Completo");

CREATE TABLE IF NOT EXISTS Gene (
	id_gene INT PRIMARY KEY,
    nome VARCHAR(255)
);

INSERT INTO Gene VALUES
    (0, "BCRA1"),
    (1, "BCRA2"),
    (2, "PKU");

CREATE TABLE IF NOT EXISTS ResultadoGenetico (
	id_paciente INT,
    id_gene INT,
    id_tipo_proc INT,
    resultado BOOLEAN,
    
    PRIMARY KEY (id_paciente, id_gene),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_gene) REFERENCES Gene(id_gene),
    FOREIGN KEY (id_tipo_proc) REFERENCES TipoProcedimento(id_tipo_proc)
);