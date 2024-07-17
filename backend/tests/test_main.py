from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.models import Paises, TipoGenero, SituacaoConjugal, GrauInstrucao, Raca, Estado, TipoDoencas, TipoCancer, OpcaoTriviais, GrauParentesco, Origem, ParenteSangue, Paciente, PacienteCancer, PacienteLesao, Parente, ParenteDoenca, ParenteCancer
from app.database import Base
from app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

db = TestingSessionLocal()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API FORMULARIO A. C. Camargo"}

def test_read_paises():
    db_object = Paises(**{'id_pais': 1, 'nome': 'Brazil'})
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    db.close()
    response = client.get("/paises/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_pais': 1, 'nome': 'Brazil'}

def teste_read_genero():
    db_object = TipoGenero(nome = 'Masculino')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/genero/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_genero': db_object.id_genero, 'nome': 'Masculino'}
    db.close()

def teste_read_situacao_conjugal():
    db_object = SituacaoConjugal(nome_situacao = 'solteiro(a)')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/situacao_conjugal/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_situacao': db_object.id_situacao, 'nome_situacao': 'solteiro(a)'}
    db.close()

def test_read_grau_instrucao():
    db_object = GrauInstrucao(nome_intrucao = 'Ensino superior completo')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/grau_instrucao/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_instrucao': db_object.id_instrucao, 'nome_intrucao': 'Ensino superior completo'}
    db.close()

def teste_read_raca():
    db_object = Raca(nome_raca = 'Branco/pele clara/clara')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/raca/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_raca': db_object.id_raca, 'nome_raca': 'Branco/pele clara/clara'}
    db.close()

def teste_read_estado():
    db_object = Estado(nome_estado = 'Sao Paulo')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/estado/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_estado': db_object.id_estado, 'nome_estado': 'Sao Paulo'}
    db.close()

def test_read_tipo_dienca():
    db_object = TipoDoencas(nome_doenca = 'Derrame cerebral/AVC/isquemia cerebral')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/tipo_doencas/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_doenca': db_object.id_doenca, 'nome_doenca': 'Derrame cerebral/AVC/isquemia cerebral'}
    db.close()

def test_read_tipo_cancer():
    db_object = TipoCancer(nome = 'Ovário')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/tipo_cancer/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_cancer': db_object.id_cancer, 'nome': 'Ovário'}
    db.close()

def test_read_opcao_triviais():
    db_object = OpcaoTriviais(opcao = 'Sim')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/opcao_triviais/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_opcao': db_object.id_opcao, 'opcao': 'Sim'}
    db.close()

def test_read_grau_parentesco():
    db_object = GrauParentesco(nome = 'pai')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/grau_parentesco/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_parentesco': db_object.id_parentesco, 'nome': 'pai'}
    db.close()

def test_read_origem():
    db_object = Origem(nome_origem = 'brasileiro')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/origem/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_origem': db_object.id_origem, 'nome_origem': 'brasileiro'}
    db.close()

def test_read_parente_sangue():
    db_object = ParenteSangue(nome = 'Não são da mesma família')
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    response = client.get("/parente_sangue/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {'id_parentesco': db_object.id_parentesco, 'nome': 'Não são da mesma família'}

def test_create_paciente():
    
    paciente_data = {
        "quem_respondeu": "Médico",
        "paciente": True,
        "rgh": "12345678",
        "cpf": "123.456.789-10",
        "nome_paciente": "João Silva",
        "nome_mae": "Maria Silva",
        "genero_id": 1,
        "data_nascimento": "1990-01-01",
        "pais_residente_id": 1,
        "cidade_residente": "São Paulo",
        "estado_residente_id": 1,
        "cep_residente": "12345-678",
        "telefone": "11 98765-4321",
        "email": "joao.silva@example.com"
    }
    
    response = client.post("/paciente/", json=paciente_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["quem_respondeu"] == paciente_data["quem_respondeu"]
    assert response_data["cpf"] == paciente_data["cpf"]
    assert response_data["email"] == paciente_data["email"]

    db_patient = db.query(Paciente).filter(Paciente.cpf == "123.456.789-10").first()
    assert db_patient is not None
    assert db_patient.nome_paciente == "João Silva"

    db.close()


def test_create_paciente_doenca():

    paciente_doenca_data = {
        "id_paciente": 1,
        "id_doenca": 1,
        "doenca_outro": "Detalhes adicionais sobre a doença"
    }

    response = client.post("/paciente_doenca/", json=paciente_doenca_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_paciente'] == paciente_doenca_data['id_paciente']
    assert response_data['id_doenca'] == paciente_doenca_data['id_doenca']
    assert response_data['doenca_outro'] == paciente_doenca_data['doenca_outro']

    db.close()

def test_create_paciente_cancer():

    paciente_cancer_data = {
        "id_paciente": 1,
        "id_cancer": 1,
        "idade": 45,
        "cancer_outro": "Informações adicionais sobre o câncer"
    }

    response = client.post("/paciente_cancer/", json=paciente_cancer_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_paciente'] == paciente_cancer_data['id_paciente']
    assert response_data['id_cancer'] == paciente_cancer_data['id_cancer']
    assert response_data['idade'] == 45
    assert response_data['cancer_outro'] == "Informações adicionais sobre o câncer"

    db_relation = db.query(PacienteCancer).filter_by(id_paciente=1, id_cancer=1).first()
    assert db_relation is not None
    assert db_relation.idade == 45
    assert db_relation.cancer_outro == "Informações adicionais sobre o câncer"

    db.close()


def test_create_paciente_lesao():

    paciente_lesao_data = {
        "id_paciente": 1,
        "id_lesao": 1,
        "idade": 40
    }

    response = client.post("/paciente_lesao/", json=paciente_lesao_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_paciente'] == paciente_lesao_data['id_paciente']
    assert response_data['id_lesao'] == paciente_lesao_data['id_lesao']
    assert response_data['idade'] == 40

    db_relation = db.query(PacienteLesao).filter_by(id_paciente=1, id_lesao=1).first()
    assert db_relation is not None
    assert db_relation.idade == 40

    db.close()

def test_create_parente():

    parente_data = {
        "id_paciente": 1,
        "id_parentesco": 1
    }

    response = client.post("/parente/", json=parente_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_paciente'] == parente_data['id_paciente']
    assert response_data['id_parentesco'] == parente_data['id_parentesco']

    db_parente = db.query(Parente).filter_by(id_paciente=1, id_parentesco=1).first()
    assert db_parente is not None

    db.close()

def test_create_parente_doenca():

    parente_doenca_data = {
        "id_paciente": 1,
        "id_doenca_familia": 1,
        "doenca_familia_outro": "Histórico familiar de diabetes"
    }

    response = client.post("/parente_doenca/", json=parente_doenca_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_paciente'] == parente_doenca_data['id_paciente']
    assert response_data['id_doenca_familia'] == parente_doenca_data['id_doenca_familia']
    assert response_data['doenca_familia_outro'] == "Histórico familiar de diabetes"

    db_relation = db.query(ParenteDoenca).filter_by(id_paciente=1, id_doenca_familia=1).first()
    assert db_relation is not None
    assert db_relation.doenca_familia_outro == "Histórico familiar de diabetes"

    db.close()

def test_create_parente_cancer():

    parente_cancer_data = {
        "id_parente": 1,
        "id_cancer": 1,
        "idade": 52,
        "cancer_outro": "Diagnóstico confirmado recentemente"
    }

    response = client.post("/parente_cancer/", json=parente_cancer_data)
    
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id_parente'] == parente_cancer_data['id_parente']
    assert response_data['id_cancer'] == parente_cancer_data['id_cancer']
    assert response_data['idade'] == 52
    assert response_data['cancer_outro'] == "Diagnóstico confirmado recentemente"

    db_relation = db.query(ParenteCancer).filter_by(id_parente=1, id_cancer=1).first()
    assert db_relation is not None
    assert db_relation.idade == 52
    assert db_relation.cancer_outro == "Diagnóstico confirmado recentemente"

    db.close()