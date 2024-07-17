CREATE DATABASE IF NOT EXISTS pfe_dev;

USE pfe_dev;

CREATE TABLE IF NOT EXISTS TipoGenero (
    id_genero INT PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL
);

INSERT INTO TipoGenero VALUES
    (0, "Masculino"),
    (1, "Feminino"),
    (2, "Outros");

CREATE TABLE IF NOT EXISTS Paises (
    id_pais INT PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL
);

INSERT INTO Paises VALUES
	(35, "Brasil"),
	(1, "Afeganistão"),
	(2, "África do Sul"),
	(3, "Akrotiri"),
	(4, "Albânia"),
	(5, "Alemanha"),
	(6, "Andorra"),
	(7, "Angola"),
	(8, "Anguila"),
	(9, "Antárctida"),
	(10, "Antígua e Barbuda"),
	(11, "Arábia Saudita"),
	(12, "Arctic Ocean"),
	(13, "Argélia"),
	(14, "Argentina"),
	(15, "Arménia"),
	(16, "Aruba"),
	(17, "Ashmore and Cartier Islands"),
	(18, "Atlantic Ocean"),
	(19, "Austrália"),
	(20, "Áustria"),
	(21, "Azerbaijão"),
	(22, "Baamas"),
	(23, "Bangladeche"),
	(24, "Barbados"),
	(25, "Barém"),
	(26, "Bélgica"),
	(27, "Belize"),
	(28, "Benim"),
	(29, "Bermudas"),
	(30, "Bielorrússia"),
	(31, "Birmânia"),
	(32, "Bolívia"),
	(33, "Bósnia e Herzegovina"),
	(34, "Botsuana"),
	(36, "Brunei"),
	(37, "Bulgária"),
	(38, "Burquina Faso"),
	(39, "Burúndi"),
	(40, "Butão"),
	(41, "Cabo Verde"),
	(42, "Camarões"),
	(43, "Camboja"),
	(44, "Canadá"),
	(45, "Catar"),
	(46, "Cazaquistão"),
	(47, "Chade"),
	(48, "Chile"),
	(49, "China"),
	(50, "Chipre"),
	(51, "Clipperton Island"),
	(52, "Colômbia"),
	(53, "Comores"),
	(54, "Congo-Brazzaville"),
	(55, "Congo-Kinshasa"),
	(56, "Coral Sea Islands"),
	(57, "Coreia do Norte"),
	(58, "Coreia do Sul"),
	(59, "Costa do Marfim"),
	(60, "Costa Rica"),
	(61, "Croácia"),
	(62, "Cuba"),
	(63, "Curacao"),
	(64, "Dhekelia"),
	(65, "Dinamarca"),
	(66, "Domínica"),
	(67, "Egipto"),
	(68, "Emiratos Árabes Unidos"),
	(69, "Equador"),
	(70, "Eritreia"),
	(71, "Eslováquia"),
	(72, "Eslovénia"),
	(73, "Espanha"),
	(74, "Estados Unidos"),
	(75, "Estónia"),
	(76, "Etiópia"),
	(77, "Faroé"),
	(78, "Fiji"),
	(79, "Filipinas"),
	(80, "Finlândia"),
	(81, "França"),
	(82, "Gabão"),
	(83, "Gâmbia"),
	(84, "Gana"),
	(85, "Gaza Strip"),
	(86, "Geórgia"),
	(87, "Geórgia do Sul e Sandwich do Sul"),
	(88, "Gibraltar"),
	(89, "Granada"),
	(90, "Grécia"),
	(91, "Gronelândia"),
	(92, "Guame"),
	(93, "Guatemala"),
	(94, "Guernsey"),
	(95, "Guiana"),
	(96, "Guiné"),
	(97, "Guiné Equatorial"),
	(98, "Guiné-Bissau"),
	(99, "Haiti"),
	(100, "Honduras"),
	(101, "Hong Kong"),
	(102, "Hungria"),
	(103, "Iémen"),
	(104, "Ilha Bouvet"),
	(105, "Ilha do Natal"),
	(106, "Ilha Norfolk"),
	(107, "Ilhas Caimão"),
	(108, "Ilhas Cook"),
	(109, "Ilhas dos Cocos"),
	(110, "Ilhas Falkland"),
	(111, "Ilhas Heard e McDonald"),
	(112, "Ilhas Marshall"),
	(113, "Ilhas Salomão"),
	(114, "Ilhas Turcas e Caicos"),
	(115, "Ilhas Virgens Americanas"),
	(116, "Ilhas Virgens Britânicas"),
	(117, "Índia"),
	(118, "Indian Ocean"),
	(119, "Indonésia"),
	(120, "Irão"),
	(121, "Iraque"),
	(122, "Irlanda"),
	(123, "Islândia"),
	(124, "Israel"),
	(125, "Itália"),
	(126, "Jamaica"),
	(127, "Jan Mayen"),
	(128, "Japão"),
	(129, "Jersey"),
	(130, "Jibuti"),
	(131, "Jordânia"),
	(132, "Kosovo"),
	(133, "Kuwait"),
	(134, "Laos"),
	(135, "Lesoto"),
	(136, "Letónia"),
	(137, "Líbano"),
	(138, "Libéria"),
	(139, "Líbia"),
	(140, "Listenstaine"),
	(141, "Lituânia"),
	(142, "Luxemburgo"),
	(143, "Macau"),
	(144, "Macedónia"),
	(145, "Madagáscar"),
	(146, "Malásia"),
	(147, "Malávi"),
	(148, "Maldivas"),
	(149, "Mali"),
	(150, "Malta"),
	(151, "Marianas do Norte"),
	(152, "Marrocos"),
	(153, "Maurícia"),
	(154, "Mauritânia"),
	(155, "México"),
	(156, "Micronésia"),
	(157, "Moçambique"),
	(158, "Moldávia"),
	(159, "Mónaco"),
	(160, "Mongólia"),
	(161, "Monserrate"),
	(162, "Montenegro"),
	(163, "Mundo"),
	(164, "Namíbia"),
	(165, "Nauru"),
	(166, "Navassa Island"),
	(167, "Nepal"),
	(168, "Nicarágua"),
	(169, "Níger"),
	(170, "Nigéria"),
	(171, "Niue"),
	(172, "Noruega"),
	(173, "Nova Caledónia"),
	(174, "Nova Zelândia"),
	(175, "Omã"),
	(176, "Pacific Ocean"),
	(177, "Países Baixos"),
	(178, "Palau"),
	(179, "Panamá"),
	(180, "Papua-Nova Guiné"),
	(181, "Paquistão"),
	(182, "Paracel Islands"),
	(183, "Paraguai"),
	(184, "Peru"),
	(185, "Pitcairn"),
	(186, "Polinésia Francesa"),
	(187, "Polónia"),
	(188, "Porto Rico"),
	(189, "Portugal"),
	(190, "Quénia"),
	(191, "Quirguizistão"),
	(192, "Quiribáti"),
	(193, "Reino Unido"),
	(194, "República Centro-Africana"),
	(195, "República Checa"),
	(196, "República Dominicana"),
	(197, "Roménia"),
	(198, "Ruanda"),
	(199, "Rússia"),
	(200, "Salvador"),
	(201, "Samoa"),
	(202, "Samoa Americana"),
	(203, "Santa Helena"),
	(204, "Santa Lúcia"),
	(205, "São Bartolomeu"),
	(206, "São Cristóvão e Neves"),
	(207, "São Marinho"),
	(208, "São Martinho"),
	(209, "São Pedro e Miquelon"),
	(210, "São Tomé e Príncipe"),
	(211, "São Vicente e Granadinas"),
	(212, "Sara Ocidental"),
	(213, "Seicheles"),
	(214, "Senegal"),
	(215, "Serra Leoa"),
	(216, "Sérvia"),
	(217, "Singapura"),
	(218, "Sint Maarten"),
	(219, "Síria"),
	(220, "Somália"),
	(221, "Southern Ocean"),
	(222, "Spratly Islands"),
	(223, "Sri Lanca"),
	(224, "Suazilândia"),
	(225, "Sudão"),
	(226, "Sudão do Sul"),
	(227, "Suécia"),
	(228, "Suíça"),
	(229, "Suriname"),
	(230, "Svalbard e Jan Mayen"),
	(231, "Tailândia"),
	(232, "Taiwan"),
	(233, "Tajiquistão"),
	(234, "Tanzânia"),
	(235, "Território Britânico do Oceano Índico"),
	(236, "Territórios Austrais Franceses"),
	(237, "Timor Leste"),
	(238, "Togo"),
	(239, "Tokelau"),
	(240, "Tonga"),
	(241, "Trindade e Tobago"),
	(242, "Tunísia"),
	(243, "Turquemenistão"),
	(244, "Turquia"),
	(245, "Tuvalu"),
	(246, "Ucrânia"),
	(247, "Uganda"),
	(248, "União Europeia"),
	(249, "Uruguai"),
	(250, "Usbequistão"),
	(251, "Vanuatu"),
	(252, "Vaticano"),
	(253, "Venezuela"),
	(254, "Vietname"),
	(255, "Wake Island"),
	(256, "Wallis e Futuna"),
	(257, "West Bank"),
	(258, "Zâmbia"),
	(259, "Zimbabué");
    
CREATE TABLE IF NOT EXISTS SituacaoConjugal (
    id_situacao INTEGER PRIMARY KEY NOT NULL auto_increment,
    nome_situacao VARCHAR(255) NOT NULL
);

INSERT INTO SituacaoConjugal VALUES
	(1, "solteiro(a)"),
	(2, "casado(a)/companheiro(a)/amigado(a)"),
	(3, "separado(a)/divorciado(a)"),
	(4, "viúvo(a)");
    
CREATE TABLE IF NOT EXISTS GrauInstrucao (
    id_instrucao INTEGER PRIMARY KEY NOT NULL auto_increment,
    nome_intrucao VARCHAR(255) NOT NULL
);

INSERT INTO GrauInstrucao VALUES
    (1, "Analfabeto/pré-primário"),
    (2, "Ensino primário/fundamental"),
    (3, "Ensino médio/segundo grau/normal/antigo científico/técnico"),
    (4, "Ensino superior incompleto"),
    (5, "Ensino superior completo"),
    (6, "Pós-graduação/mestrado/especialização/residência"),
    (7, "Doutorado e pós-doutorado"),
    (8, "Prefiro não responder");
 
 
CREATE TABLE IF NOT EXISTS Raca (
    id_raca INTEGER PRIMARY KEY NOT NULL auto_increment,
    nome_raca VARCHAR(255) NOT NULL
);

INSERT INTO Raca VALUES
    (1, "Branco/pele clara/clara"),
    (2, "Parda/morena/mulata/mestiça"),
    (3, "Preta/negra/africana/escura"),
    (4, "Amarela/oriental/asiática"),
    (5, "Indígena"),
    (6, "Prefiro não responder");
    
    
CREATE TABLE IF NOT EXISTS Estado (
    id_estado INTEGER PRIMARY KEY NOT NULL auto_increment,
    nome_estado VARCHAR(255) NOT NULL
);

INSERT INTO Estado VALUES
	(25,"Sao Paulo"),
	(1,"Acre"),
	(2,"Alagoas"),
	(3,"Amapa"),
	(4,"Amazonas"),
	(5,"Bahia"),
	(6,"Ceara"),
	(7,"Distrito Federal"),
	(8,"Espirito Santo"),
	(9,"Goias"),
	(10,"Maranhao"),
	(11,"Mato Grosso"),
	(12,"Mato Grosso do Sul"),
	(13,"Minas Gerais"),
	(14,"Para"),
	(15,"Paraíba"),
	(16,"Parana"),
	(17,"Pernambuco"),
	(18,"Piaui"),
	(19,"Rio de Janeiro"),
	(20,"Rio Grande do Norte"),
	(21,"Rio Grande do Sul"),
	(22,"Rondonia"),
	(23,"Roraima"),
	(24,"Santa Catarina"),
	(26,"Sergipe"),
	(27,"Tocantins");


CREATE TABLE IF NOT EXISTS TipoDoencas (
    id_doenca INTEGER PRIMARY KEY NOT NULL auto_increment,
    nome_doenca VARCHAR(255) NOT NULL
);

INSERT INTO TipoDoencas VALUES
	(1, "Pressão arterial alta/hipertensão"),
	(2, "Diabetes"),
	(3, "Obesidade"),
	(4, "Infarto cardíaco/problema de coronárias/angina"),
	(5, "Derrame cerebral/AVC/isquemia cerebral"),
	(6, "Trombose nas pernas/braços"),
	(7, "Depressão grave"),
	(8, "Autismo/distúrbio de atenção"),
	(9, "Malformação congênita"),
	(10, "Outro");
    
CREATE TABLE IF NOT EXISTS TipoCancer (
    id_cancer INT PRIMARY KEY NOT NULL,
    nome VARCHAR(255)
);

INSERT INTO TipoCancer VALUES
    (-1, "Não sei se tenho"),
    (0, "Não sei onde começou"),
    (1, "Pulmão"),
    (2, "Ovário"),
    (3, "Estômago"),
    (4, "Pele"),
    (5, "Leucemia"),
    (6, "Intestino"),
    (7, "Cabeça e Pescoço"),
    (8, "Mama"),
    (9, "Próstata"),
    (10, "Tireóide"),
    (11, "Cerebral/sistema nervoso central"),
    (12, "Bexiga"),
    (13, "Linfoma"),
    (14, "Braços/pernas"),
    (15, "Outro");

CREATE TABLE IF NOT EXISTS OpcaoTriviais (
    id_opcao INT PRIMARY KEY NOT NULL,
    opcao VARCHAR(255)
);

INSERT INTO OpcaoTriviais VALUES
    (1, "Não"),
    (2, "Sim"),
    (3, "Não sei");

CREATE TABLE IF NOT EXISTS GrauParentesco (
    id_parentesco INT PRIMARY KEY NOT NULL,
    nome VARCHAR(255)
);

INSERT INTO GrauParentesco VALUES
    (1, "filho"),
    (2, "filha"),
    (3, "pai"),
    (4, "mãe"),
    (5, "avô paterno"),
    (6, "avó paterna"),
    (7, "avô materno"),
    (8, "avó materna"),
    (9, "irmão"),
    (10, "irmã"),
    (11, "tio paterno"),
    (12, "tia paterno"),
    (13, "tio materno"),
    (14, "tia materno"),
    (15, "primos paternos"),
    (16, "primos maternos"),
    (17, "sobrinhos paternos"),
    (18, "sobrinhos maternos"),
    (19, "netos");

CREATE TABLE IF NOT EXISTS Origem (
    id_origem INT PRIMARY KEY NOT NULL,
    nome_origem VARCHAR(255)
);

INSERT INTO Origem VALUES
    (1, "brasileiro"),
    (2, "judeu ashkenazi"),
    (3, "judeu sefaradita"),
    (4, "indígena"),
    (5, "afrodescente"),
    (6, "alemão"),
    (7, "português"),
    (8, "espanhol"),
    (9, "sírio-libanês"),
    (10, "italiano"),
    (11, "japônes"),
    (12, "polonês"),
    (13, "ucraniana"),
    (14, "não sei"),
    (15, "outra");
    
    
CREATE TABLE IF NOT EXISTS ParenteSangue (
    id_parentesco INT PRIMARY KEY NOT NULL,
    nome VARCHAR(255)
);

INSERT INTO ParenteSangue VALUES
    (1, "Não são da mesma família"),
    (2, "São parentes/primos"),
    (3, "Não sei");

CREATE TABLE IF NOT EXISTS Paciente (
    id_paciente INTEGER PRIMARY KEY NOT NULL auto_increment,
    quem_respondeu VARCHAR(255) NOT NULL,
    paciente BOOLEAN, 
    rgh VARCHAR(255),
    cpf VARCHAR(255) NOT NULL,
    nome_paciente VARCHAR(255),
    nome_mae VARCHAR(255),
    genero_id INT,
    data_nascimento DATE,
    pais_residente_id INT,
    cidade_residente VARCHAR(255),
    estado_residente_id INT,
    cep_residente VARCHAR(255),
    situacao_conjugal_id INT,
    grau_instrucao_id INT,
    cor_raca_id INT,
    ocupacao VARCHAR(255),
    tempo_ocupacao INTEGER,
    telefone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    idade INTEGER,
    pais_origem_id INT,
    cidade_origem VARCHAR(255),
    estado_origem_id INT,
    adotado BOOLEAN,
    cancer BOOLEAN,
    cancer_hereditario_id INT,
    teste_genetico_id INT,
    informacoes_corretas BOOLEAN,
    parentesco_pais_id INT,
    parentesco_avosm_id INT,
    parentesco_avosp_id INT,
    
    FOREIGN KEY (genero_id) REFERENCES TipoGenero(id_genero),
    FOREIGN KEY (pais_residente_id) REFERENCES Paises(id_pais),
    FOREIGN KEY (estado_residente_id) REFERENCES Estado(id_estado),
    FOREIGN KEY (situacao_conjugal_id) REFERENCES SituacaoConjugal(id_situacao),
    FOREIGN KEY (grau_instrucao_id) REFERENCES GrauInstrucao(id_instrucao),
    FOREIGN KEY (cor_raca_id) REFERENCES Raca(id_raca),
    FOREIGN KEY (pais_origem_id) REFERENCES Paises(id_pais),
    FOREIGN KEY (estado_origem_id) REFERENCES Estado(id_estado),
    FOREIGN KEY (estado_residente_id) REFERENCES Estado(id_estado),
    FOREIGN KEY (cancer_hereditario_id) REFERENCES OpcaoTriviais(id_opcao),
    FOREIGN KEY (teste_genetico_id) REFERENCES OpcaoTriviais(id_opcao),
    FOREIGN KEY (parentesco_pais_id) REFERENCES ParenteSangue(id_parentesco),
    FOREIGN KEY (parentesco_avosm_id) REFERENCES ParenteSangue(id_parentesco),
    FOREIGN KEY (parentesco_avosp_id) REFERENCES ParenteSangue(id_parentesco)
);

CREATE TABLE IF NOT EXISTS PacienteDoenca (
    id_paciente INT NOT NULL,
    id_doenca INT NOT NULL,
    doenca_outro VARCHAR(255),
    PRIMARY KEY (id_paciente, id_doenca),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_doenca) REFERENCES TipoDoencas(id_doenca)
);

CREATE TABLE IF NOT EXISTS PacienteCancer (
    id_paciente INT NOT NULL,
    id_cancer INT NOT NULL,
    idade INT,
    cancer_outro VARCHAR(255),
    PRIMARY KEY (id_paciente, id_cancer),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_cancer) REFERENCES TipoCancer(id_cancer)
);

CREATE TABLE IF NOT EXISTS PacienteLesao (
    id_paciente INT NOT NULL,
    id_lesao INT NOT NULL,
    idade INT,
    PRIMARY KEY (id_paciente, id_lesao),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_lesao) REFERENCES TipoCancer(id_cancer)
);

CREATE TABLE IF NOT EXISTS Parente (
    id_parente INTEGER PRIMARY KEY NOT NULL auto_increment,
    id_paciente INT NOT NULL,
    id_parentesco INT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_parentesco) REFERENCES GrauParentesco(id_parentesco)
);

CREATE TABLE IF NOT EXISTS ParenteDoenca (
    id_paciente INT NOT NULL,
    id_doenca_familia INT NOT NULL,
    PRIMARY KEY (id_paciente, id_doenca_familia),
    doenca_familia_outro VARCHAR(255),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_doenca_familia) REFERENCES TipoDoencas(id_doenca)
);

CREATE TABLE IF NOT EXISTS ParenteCancer (
    id_parente INT NOT NULL,
    id_cancer INT NOT NULL,
    idade INT,
    PRIMARY KEY (id_parente, id_cancer),
    cancer_outro VARCHAR(255),
    FOREIGN KEY (id_parente) REFERENCES Parente(id_parente),
    FOREIGN KEY (id_cancer) REFERENCES TipoCancer(id_cancer)
);

CREATE TABLE IF NOT EXISTS OrigemParente (
    id_origem INT NOT NULL,
    id_parente INT NOT NULL,
    PRIMARY KEY (id_origem, id_parente),
    FOREIGN KEY (id_parente) REFERENCES Parente(id_parente),
    FOREIGN KEY (id_origem) REFERENCES Origem(id_origem)
);