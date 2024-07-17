from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Paciente(Base):
    __tablename__ = "Paciente"

    id_paciente = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    quem_respondeu = Column(String(255), nullable=False)
    paciente = Column(Boolean)
    rgh = Column(String(255))
    cpf = Column(String(255), nullable=False)
    nome_paciente = Column(String(255))
    nome_mae = Column(String(255))
    genero_id = Column(Integer, ForeignKey("TipoGenero.id_genero"))
    data_nascimento = Column(Date)
    pais_residente_id = Column(Integer, ForeignKey("Paises.id_pais"))
    cidade_residente = Column(String(255))
    estado_residente_id = Column(Integer, ForeignKey("Estado.id_estado"))
    cep_residente = Column(String(255))
    situacao_conjugal_id = Column(Integer, ForeignKey("SituacaoConjugal.id_situacao"))
    grau_instrucao_id = Column(Integer, ForeignKey("GrauInstrucao.id_instrucao"))
    cor_raca_id = Column(Integer, ForeignKey("Raca.id_raca"))
    ocupacao = Column(String(255))
    tempo_ocupacao = Column(Integer)
    telefone = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    idade = Column(Integer)
    pais_origem_id = Column(Integer, ForeignKey("Paises.id_pais"))
    cidade_origem = Column(String(255))
    estado_origem_id = Column(Integer, ForeignKey("Estado.id_estado"))
    adotado = Column(Boolean)
    cancer = Column(Boolean)
    cancer_hereditario_id = Column(Integer, ForeignKey("OpcaoTriviais.id_opcao"))
    teste_genetico_id = Column(Integer, ForeignKey("OpcaoTriviais.id_opcao"))
    informacoes_corretas = Column(Boolean)
    parentesco_pais_id = Column(Integer, ForeignKey("ParenteSangue.id_parentesco"))
    parentesco_avosm_id = Column(Integer, ForeignKey("ParenteSangue.id_parentesco"))
    parentesco_avosp_id = Column(Integer, ForeignKey("ParenteSangue.id_parentesco"))

    genero = relationship("TipoGenero", back_populates="paciente_genero")
    pais_residente = relationship("Paises", foreign_keys=[pais_residente_id], back_populates="paciente_residente")
    estado_residente = relationship("Estado", foreign_keys=[estado_residente_id], back_populates="paciente_estado_residente")
    situacao_conjugal = relationship("SituacaoConjugal", back_populates="paciente_conjugal")
    grau_instrucao = relationship("GrauInstrucao", back_populates="paciente_grau_instrucao")
    cor_raca = relationship("Raca", back_populates="paciente_raca")
    pais_origem = relationship("Paises", foreign_keys=[pais_origem_id], back_populates="paciente_origem")
    estado_origem = relationship("Estado", foreign_keys=[estado_origem_id], back_populates="paciente_estado_origem")
    cancer_hereditario = relationship("OpcaoTriviais", foreign_keys=[cancer_hereditario_id], back_populates="paciente_cancer_hereditico")
    teste_genetico = relationship("OpcaoTriviais", foreign_keys=[teste_genetico_id], back_populates="paciente_teste_genetico")
    parentesco_pais = relationship("ParenteSangue", foreign_keys=[parentesco_pais_id], back_populates="paciente_pais_parentes")
    parentesco_avosm = relationship("ParenteSangue", foreign_keys=[parentesco_avosm_id], back_populates="paciente_avosm_parentes")
    parentesco_avosp = relationship("ParenteSangue", foreign_keys=[parentesco_avosp_id], back_populates="paciente_avosp_parentes")


    doencas = relationship("PacienteDoenca", back_populates="paciente")
    cancers = relationship("PacienteCancer", back_populates="paciente_cancer")
    parentes = relationship("Parente", back_populates="paciente")
    doenca_familia = relationship("ParenteDoenca", back_populates="parentes_doenca")
    lesoes = relationship("PacienteLesao", back_populates="paciente_lesao")

class Paises(Base):
    __tablename__ = 'Paises'

    id_pais = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome = Column(String(255), nullable=False)

    paciente_residente = relationship("Paciente", foreign_keys="Paciente.pais_residente_id", back_populates="pais_residente")
    paciente_origem = relationship("Paciente", foreign_keys="Paciente.pais_origem_id", back_populates="pais_origem")

class TipoGenero(Base):
    __tablename__ = 'TipoGenero'

    id_genero = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome = Column(String(255), nullable=False)

    paciente_genero = relationship("Paciente", back_populates="genero")

class SituacaoConjugal(Base):
    __tablename__ = 'SituacaoConjugal'

    id_situacao = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_situacao = Column(String(255), nullable=False)

    paciente_conjugal = relationship("Paciente", back_populates="situacao_conjugal")

class GrauInstrucao(Base):
    __tablename__ = 'GrauInstrucao'

    id_instrucao = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_intrucao = Column(String(255), nullable=False)

    paciente_grau_instrucao = relationship("Paciente", back_populates="grau_instrucao")

class Raca(Base):
    __tablename__ = 'Raca'

    id_raca = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_raca = Column(String(255), nullable=False)

    paciente_raca = relationship("Paciente", back_populates="cor_raca")

class Estado(Base):
    __tablename__ = 'Estado'

    id_estado = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_estado = Column(String(255), nullable=False)

    paciente_estado_residente = relationship("Paciente", foreign_keys="Paciente.estado_residente_id", back_populates="estado_residente")
    paciente_estado_origem = relationship("Paciente", foreign_keys="Paciente.estado_origem_id", back_populates="estado_origem")

class TipoDoencas(Base):
    __tablename__ = 'TipoDoencas'

    id_doenca = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_doenca = Column(String(255), nullable=False)

    pacientes = relationship("PacienteDoenca", back_populates="doenca")
    parentes = relationship("ParenteDoenca", back_populates="doenca_parente")


class TipoCancer(Base):
    __tablename__ = 'TipoCancer'

    id_cancer = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome = Column(String(255), nullable=False)

    pacientes_cancer = relationship("PacienteCancer", back_populates="tipo_cancer")
    parentes_cancer = relationship("ParenteCancer", back_populates="tipo_cancer")
    pacientes_lesao = relationship("PacienteLesao", back_populates="tipo_lesao")

class OpcaoTriviais(Base):
    __tablename__ = 'OpcaoTriviais'

    id_opcao = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    opcao = Column(String(255), nullable=False)

    paciente_cancer_hereditico = relationship("Paciente", foreign_keys="Paciente.cancer_hereditario_id", back_populates="cancer_hereditario")
    paciente_teste_genetico = relationship("Paciente", foreign_keys="Paciente.teste_genetico_id", back_populates="teste_genetico")

class GrauParentesco(Base):
    __tablename__ = 'GrauParentesco'

    id_parentesco = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome = Column(String(255), nullable=False)

    parentes = relationship("Parente", back_populates="parentesco")

class Origem(Base):
    __tablename__ = 'Origem'

    id_origem = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome_origem = Column(String(255), nullable=False)

class ParenteSangue(Base):
    __tablename__ = 'ParenteSangue'

    id_parentesco = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    nome = Column(String(255), nullable=False)

    paciente_pais_parentes = relationship("Paciente", foreign_keys="Paciente.parentesco_pais_id",back_populates="parentesco_pais")
    paciente_avosm_parentes = relationship("Paciente", foreign_keys="Paciente.parentesco_avosm_id", back_populates="parentesco_avosm")
    paciente_avosp_parentes = relationship("Paciente", foreign_keys="Paciente.parentesco_avosp_id", back_populates="parentesco_avosp")


class PacienteDoenca(Base):
    __tablename__ = 'PacienteDoenca'
    
    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"), primary_key=True)
    id_doenca = Column(Integer, ForeignKey("TipoDoencas.id_doenca"), primary_key=True)
    doenca_outro = Column(String(255))

    paciente = relationship("Paciente", back_populates="doencas")
    doenca = relationship("TipoDoencas", back_populates="pacientes")


class PacienteCancer(Base):
    __tablename__ = 'PacienteCancer'

    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"), primary_key=True)
    id_cancer = Column(Integer, ForeignKey("TipoCancer.id_cancer"), primary_key=True)
    idade = Column(Integer)
    cancer_outro = Column(String(255))

    paciente_cancer = relationship("Paciente", back_populates="cancers")
    tipo_cancer = relationship("TipoCancer", back_populates="pacientes_cancer")

class PacienteLesao(Base):
    __tablename__ = 'PacienteLesao'

    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"), primary_key=True)
    id_lesao = Column(Integer, ForeignKey("TipoCancer.id_cancer"), primary_key=True)
    idade = Column(Integer)

    paciente_lesao = relationship("Paciente", back_populates="lesoes")
    tipo_lesao = relationship("TipoCancer", back_populates="pacientes_lesao")

class Parente(Base):
    __tablename__ = 'Parente'

    id_parente = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True, index=True)
    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"))
    id_parentesco = Column(Integer, ForeignKey("GrauParentesco.id_parentesco"))

    paciente = relationship("Paciente", back_populates="parentes")
    parentesco = relationship("GrauParentesco", back_populates="parentes")
    cancer_parente = relationship("ParenteCancer", back_populates="parente_cancer")


class ParenteDoenca(Base):
    __tablename__ = 'ParenteDoenca'

    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"), primary_key=True)
    id_doenca_familia = Column(Integer, ForeignKey("TipoDoencas.id_doenca"), primary_key=True)
    doenca_familia_outro = Column(String(255))


    parentes_doenca = relationship("Paciente", back_populates="doenca_familia")
    doenca_parente = relationship("TipoDoencas", back_populates="parentes")

class ParenteCancer(Base):
    __tablename__ = 'ParenteCancer'

    id_parente = Column(Integer, ForeignKey("Parente.id_parente"), primary_key=True)
    id_cancer = Column(Integer, ForeignKey("TipoCancer.id_cancer"), primary_key=True)
    idade = Column(Integer)
    cancer_outro = Column(String(255))

    parente_cancer = relationship("Parente", back_populates="cancer_parente")
    tipo_cancer = relationship("TipoCancer", back_populates="parentes_cancer")