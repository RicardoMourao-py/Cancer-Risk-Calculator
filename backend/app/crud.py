from sqlalchemy.orm import Session
from typing import Any
from . import models, schemas

def get_generic(db: Session, model_class):
    return db.query(model_class).all()

def post_generic(db: Session, schema_data, model_class):
    db_object = model_class(**schema_data.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def get_paises(db: Session):
    return get_generic(db, models.Paises)

def get_genero(db: Session):
    return get_generic(db, models.TipoGenero)

def get_situacao_conjugal(db: Session):
    return get_generic(db, models.SituacaoConjugal)

def get_grau_instrucao(db: Session):
    return get_generic(db, models.GrauInstrucao)

def get_raca(db: Session):
    return get_generic(db, models.Raca)

def get_estado(db: Session):
    return get_generic(db, models.Estado)

def get_tipo_doencas(db: Session):
    return get_generic(db, models.TipoDoencas)

def get_tipo_cancer(db: Session):
    return get_generic(db, models.TipoCancer)

def get_opcao_triviais(db: Session):
    return get_generic(db, models.OpcaoTriviais)

def get_grau_parentesco(db: Session):
    return get_generic(db, models.GrauParentesco)

def get_origem(db: Session):
    return get_generic(db, models.Origem)

def get_parente_sangue(db: Session):
    return get_generic(db, models.ParenteSangue)

def get_id_by_name(db: Session, model: Any, name_column: str, name_value: str, id_column: str):
    result =  db.query(model).filter(getattr(model, name_column) == name_value).first()
    if result is None:
        return None
    return getattr(result, id_column)

def post_paciente(db: Session, paciente: schemas.PacienteBase):
    return post_generic(db, paciente, models.Paciente)

def post_paciente_doenca(db: Session, paciente_doenca: schemas.PacienteDoencaBase):
    return post_generic(db, paciente_doenca, models.PacienteDoenca)

def post_paciente_cancer(db: Session, paciente_cancer: schemas.PacienteCancerBase):
    return post_generic(db, paciente_cancer, models.PacienteCancer)

def post_paciente_lesao(db: Session, paciente_lesao: schemas.PacienteLesaoBase):
    return post_generic(db, paciente_lesao, models.PacienteLesao)

def post_parente(db: Session, parente: schemas.ParenteBase):
    return post_generic(db, parente, models.Parente)

def post_parente_doenca(db: Session, parente_doenca: schemas.ParenteDoencaBase):
    return post_generic(db, parente_doenca, models.ParenteDoenca)

def post_parente_cancer(db: Session, parente_cancer: schemas.ParenteCancerBase):
    return post_generic(db, parente_cancer, models.ParenteCancer)

    

