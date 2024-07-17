from datetime import date
from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    quem_respondeu: Optional[str]
    paciente: bool
    rgh: Optional[str]
    cpf: Optional[str]
    nome_paciente: Optional[str] 
    nome_mae: Optional[str] 
    genero_id: Optional[int]
    data_nascimento: Optional[date]
    pais_residente_id: Optional[int]
    cidade_residente: Optional[str]
    estado_residente_id: Optional[int]
    cep_residente: Optional[str] 
    situacao_conjugal_id: Optional[int]
    grau_instrucao_id: Optional[int]
    cor_raca_id: Optional[int]
    ocupacao: Optional[str] 
    tempo_ocupacao: Optional[int] 
    telefone: Optional[str]
    email: Optional[str]
    idade: Optional[int] 
    pais_origem_id: Optional[int]
    cidade_origem: Optional[str] 
    estado_origem_id: Optional[int]
    adotado: Optional[bool] 
    cancer: Optional[bool] 
    cancer_hereditario_id: Optional[int] 
    teste_genetico_id: Optional[int] 
    informacoes_corretas: Optional[bool] 
    parentesco_pais_id: Optional[int]
    parentesco_avosm_id: Optional[int]
    parentesco_avosp_id: Optional[int]

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id_paciente: Optional[int]

    class Config:
        orm_mode = True

class PacienteDoencaBase(BaseModel):
    id_paciente: Optional[int]
    id_doenca: Optional[int]
    doenca_outro: Optional[str]

class PacienteDoencaCreate(PacienteDoencaBase):
    pass

class PacienteDoenca(PacienteDoencaBase):

    class Config:
        orm_mode = True

class PacienteCancerBase(BaseModel):
    id_paciente: Optional[int]
    id_cancer: Optional[int]
    idade: Optional[int]
    cancer_outro: Optional[str]

class PacienteCancerCreate(PacienteCancerBase):
    pass

class PacienteCancer(PacienteCancerBase):

    class Config:
        orm_mode = True

class PacienteLesaoBase(BaseModel):
    id_paciente: Optional[int]
    id_lesao: Optional[int]
    idade: Optional[int]

class PacienteLesaoCreate(PacienteLesaoBase):
    pass

class PacienteLesao(PacienteLesaoBase):
    
        class Config:
            orm_mode = True

class ParenteBase(BaseModel):
    id_paciente: Optional[int]
    id_parentesco: Optional[int]

class ParenteCreate(ParenteBase):
    pass

class Parente(ParenteBase):
    id_parente: Optional[int]

    class Config:
        orm_mode = True

class ParenteDoencaBase(BaseModel):
    id_paciente: Optional[int]
    id_doenca_familia: Optional[int]
    doenca_familia_outro: Optional[str]

class ParenteDoencaCreate(ParenteDoencaBase):
    pass

class ParenteDoenca(ParenteDoencaBase):
    
        class Config:
            orm_mode = True

class ParenteCancerBase(BaseModel):
    id_parente: Optional[int]
    id_cancer: Optional[int]
    idade: Optional[int]
    cancer_outro: Optional[str]

class ParenteCancerCreate(ParenteCancerBase):
    pass

class ParenteCancer(ParenteCancerBase):

    class Config:
        orm_mode = True