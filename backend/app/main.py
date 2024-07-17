from fastapi import FastAPI, HTTPException, Depends, Response, Query,Request
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(response: Response):
    response.headers["title"] = "Pagina Inicial"
    return {"message": "API FORMULARIO A. C. Camargo"}

@app.get("/paises/")
async def read_paises(db : Session = Depends(get_db)):
    paises = crud.get_paises(db)
    return paises

@app.get("/genero/")
async def read_genero(db : Session = Depends(get_db)):
    genero = crud.get_genero(db)
    return genero

@app.get("/situacao_conjugal/")
async def read_situacao_conjugal(db : Session = Depends(get_db)):
    situacao_conjugal = crud.get_situacao_conjugal(db)
    return situacao_conjugal

@app.get("/grau_instrucao/")
async def read_grau_instrucao(db : Session = Depends(get_db)):
    grau_instrucao = crud.get_grau_instrucao(db)
    return grau_instrucao

@app.get("/raca/")
async def read_raca(db : Session = Depends(get_db)):
    raca = crud.get_raca(db)
    return raca

@app.get("/estado/")
async def read_estado(db : Session = Depends(get_db)):
    estado = crud.get_estado(db)
    return estado

@app.get("/tipo_doencas/")
async def read_tipo_doencas(db : Session = Depends(get_db)):
    tipo_doencas = crud.get_tipo_doencas(db)
    return tipo_doencas

@app.get("/tipo_cancer/")
async def read_tipo_cancer(db : Session = Depends(get_db)):
    tipo_cancer = crud.get_tipo_cancer(db)
    return tipo_cancer

@app.get("/opcao_triviais/")
async def read_opcao_triviais(db : Session = Depends(get_db)):
    opcao_triviais = crud.get_opcao_triviais(db)
    return opcao_triviais

@app.get("/grau_parentesco/")
async def read_grau_parentesco(db : Session = Depends(get_db)):
    grau_parentesco = crud.get_grau_parentesco(db)
    return grau_parentesco

@app.get("/origem/")
async def read_origem(db : Session = Depends(get_db)):
    origem = crud.get_origem(db)
    return origem

@app.get("/parente_sangue/")
async def read_parente_sangue(db : Session = Depends(get_db)):
    return crud.get_parente_sangue(db)

@app.post("/paciente/", response_model = schemas.Paciente)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.post_paciente(db, paciente)

@app.post("/paciente_doenca/", response_model = schemas.PacienteDoenca)
def create_paciente_doenca(paciente_doenca: schemas.PacienteDoencaCreate, db: Session = Depends(get_db)):
    return crud.post_paciente_doenca(db, paciente_doenca)

@app.post("/paciente_cancer/", response_model = schemas.PacienteCancer)
def create_paciente_cancer(paciente_cancer: schemas.PacienteCancerCreate, db: Session = Depends(get_db)):
    return crud.post_paciente_cancer(db, paciente_cancer)

@app.post("/paciente_lesao/", response_model = schemas.PacienteLesao)
def create_paciente_lesao(paciente_lesao: schemas.PacienteLesaoCreate, db: Session = Depends(get_db)):
    return crud.post_paciente_lesao(db, paciente_lesao)

@app.post("/parente/", response_model = schemas.Parente)
def create_parente(parente: schemas.ParenteCreate, db: Session = Depends(get_db)):
    return crud.post_parente(db, parente)

@app.post("/parente_doenca/", response_model = schemas.ParenteDoenca)
def create_parente_doenca(parente_doenca: schemas.ParenteDoencaCreate, db: Session = Depends(get_db)):
    return crud.post_parente_doenca(db, parente_doenca)

@app.post("/parente_cancer/", response_model = schemas.ParenteCancer)
def create_parente_cancer(parente_cancer: schemas.ParenteCancerCreate, db: Session = Depends(get_db)):
    return crud.post_parente_cancer(db, parente_cancer)

@app.post("/input-predict/")
def input_predict(payload: dict, db : Session = Depends(get_db)):
    input_dict = {}
    # vc_tem_lesao_atualmente ----> opcoes_tumor
    lista_opcoes_tumor = ["Tenho tumor benigno/pólipo/nódulo benigno", "Tenho tumor maligno/câncer"]
    vc_tem_lesao_atualmente = payload.get('opcoes_tumor')
    if vc_tem_lesao_atualmente != "":
        if vc_tem_lesao_atualmente in lista_opcoes_tumor:
            input_dict['vc_tem_lesao_atualmente'] = 1
        else:
            input_dict['vc_tem_lesao_atualmente'] = 0
    else:
        input_dict['vc_tem_lesao_atualmente'] = -1

    # idade_inicio_problema_atual ----> idade_inicio_lesao
    idade_inicio_problema_atual = payload.get('idade_inicio_lesao')
    if idade_inicio_problema_atual != 0:
        input_dict['idade_inicio_problema_atual'] = int(idade_inicio_problema_atual)
    else:
        input_dict['idade_inicio_problema_atual'] = -1

    # onde_lesao ----> lesao_atual
    lesao_atual = payload.get('lesao_atual')
    if len(lesao_atual) > 0:
        lesao_atual_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', lesao_atual[0], 'id_cancer')
        input_dict['onde_lesao'] = lesao_atual_id
    else:
        input_dict['onde_lesao'] = -1

    # tipo_cancer_paciente ----> cancers_que_teve_paciente
    cancers_que_teve_paciente = payload.get('cancers_que_teve_paciente')
    if len(cancers_que_teve_paciente) > 0:
        cancers_que_teve_paciente_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancers_que_teve_paciente[0], 'id_cancer')
        input_dict['tipo_cancer_paciente'] = cancers_que_teve_paciente_id
    else:
        input_dict['tipo_cancer_paciente'] = -1

    # algum_filho_tem_ou_teve_cancer --> algum_filho_tem_ou_teve_cancer
    if payload.get('algum_filho_tem_ou_teve_cancer'): 
        input_dict['algum_filho_tem_ou_teve_cancer'] = 1
    else:
        input_dict['algum_filho_tem_ou_teve_cancer'] = 0

    # tipo_cancer_filho ----> tipo_cancer_filho
    tipo_cancer_filho = payload.get('tipo_cancer_filho')
    if len(tipo_cancer_filho) > 0:
        input_dict['tipo_cancer_filho'] = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_filho[0][0], 'id_cancer')
    else:
        input_dict['tipo_cancer_filho'] = -1

    # pai_tem_ou_teve_cancer ----> opcao_pai_cancer
    teve_cancer = payload.get('opcao_pai_cancer')
    if teve_cancer == 'Sim':
        input_dict['pai_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['pai_tem_ou_teve_cancer'] = 0
    else:
        input_dict['pai_tem_ou_teve_cancer'] = -1

    # tipo_cancer_pai ----> pai_cancer
    tipo_cancer_pai = payload.get('pai_cancer')
    if len(tipo_cancer_pai) > 0:
        tipo_cancer_pai_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_pai[0], 'id_cancer')
        input_dict['tipo_cancer_pai'] = tipo_cancer_pai_id
    else:
        input_dict['tipo_cancer_pai'] = -1

    # mae_tem_ou_teve_cancer ----> opcao_mae_cancer
    teve_cancer = payload.get('opcao_mae_cancer')
    if teve_cancer == 'Sim':
        input_dict['mae_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['mae_tem_ou_teve_cancer'] = 0
    else:
        input_dict['mae_tem_ou_teve_cancer'] = -1

    # tipo_cancer_mae ----> mae_cancer
    tipo_cancer_mae = payload.get('mae_cancer')
    if len(tipo_cancer_mae) > 0:
        tipo_cancer_mae_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_mae[0], 'id_cancer')
        input_dict['tipo_cancer_mae'] = tipo_cancer_mae_id
    else:
        input_dict['tipo_cancer_mae'] = -1

    # avo_paterno_tem_ou_teve_cancer ----> opcao_avo_paterno_cancer
    teve_cancer = payload.get('opcao_avo_paterno_cancer')
    if teve_cancer == 'Sim':
        input_dict['avo_paterno_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['avo_paterno_tem_ou_teve_cancer'] = 0
    else:
        input_dict['avo_paterno_tem_ou_teve_cancer'] = -1

    # tipo_cancer_avo_paterno ----> avo_paterno_cancer
    tipo_cancer_avo_paterno = payload.get('avo_paterno_cancer')
    if len(tipo_cancer_avo_paterno) > 0:
        tipo_cancer_avo_paterno_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_avo_paterno[0], 'id_cancer')
        input_dict['tipo_cancer_avo_paterno'] = tipo_cancer_avo_paterno_id
    else:
        input_dict['tipo_cancer_avo_paterno'] = -1

    # avo_paterna_tem_ou_teve_cancer ----> opcao_avo_paterna_cancer
    teve_cancer = payload.get('opcao_avo_paterna_cancer')
    if teve_cancer == 'Sim':
        input_dict['avo_paterna_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['avo_paterna_tem_ou_teve_cancer'] = 0
    else:
        input_dict['avo_paterna_tem_ou_teve_cancer'] = -1

    # tipo_cancer_avo_paterna ----> avo_paterna_cancer
    tipo_cancer_avo_paterna = payload.get('avo_paterna_cancer')
    if len(tipo_cancer_avo_paterna) > 0:
        tipo_cancer_avo_paterna_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_avo_paterna[0], 'id_cancer')
        input_dict['tipo_cancer_avo_paterna'] = tipo_cancer_avo_paterna_id
    else:
        input_dict['tipo_cancer_avo_paterna'] = -1
    
    # avo_materno_tem_ou_teve_cancer ----> opcao_avo_materno_cancer
    teve_cancer = payload.get('opcao_avo_materno_cancer')
    if teve_cancer == 'Sim':
        input_dict['avo_materno_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['avo_materno_tem_ou_teve_cancer'] = 0
    else:
        input_dict['avo_materno_tem_ou_teve_cancer'] = -1

    # tipo_cancer_avo_materno ----> avo_materno_cancer
    tipo_cancer_avo_materno = payload.get('avo_materno_cancer')
    if len(tipo_cancer_avo_materno) > 0:
        tipo_cancer_avo_materno_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_avo_materno[0], 'id_cancer')
        input_dict['tipo_cancer_avo_materno'] = tipo_cancer_avo_materno_id
    else:
        input_dict['tipo_cancer_avo_materno'] = -1

    # avo_materna_tem_ou_teve_cancer ----> opcao_avo_materna_cancer
    teve_cancer = payload.get('opcao_avo_materna_cancer')
    if teve_cancer == 'Sim':
        input_dict['avo_materna_tem_ou_teve_cancer'] = 1
    elif teve_cancer == 'Não':
        input_dict['avo_materna_tem_ou_teve_cancer'] = 0
    else:
        input_dict['avo_materna_tem_ou_teve_cancer'] = -1

    # tipo_cancer_avo_materna ----> avo_materna_cancer
    tipo_cancer_avo_materna = payload.get('avo_materna_cancer')
    if len(tipo_cancer_avo_materna) > 0:
        tipo_cancer_avo_materna_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', tipo_cancer_avo_materna[0], 'id_cancer')
        input_dict['tipo_cancer_avo_materna'] = tipo_cancer_avo_materna_id
    else:
        input_dict['tipo_cancer_avo_materna'] = -1

    return input_dict    

@app.post("/response/")
async def orquestra_posts(resposta: dict, db : Session = Depends(get_db)):
    ##### genero_id #####
    nome_genero = resposta.get('genero')
    genero_id = crud.get_id_by_name(db, models.TipoGenero, 'nome', nome_genero, 'id_genero')

    ##### pais_residente_id #####
    nome_pais_residente = resposta.get('pais_residente')
    pais_residente_id = crud.get_id_by_name(db, models.Paises, 'nome', nome_pais_residente, 'id_pais')

    ##### estado_residente_id #####
    nome_estado_residente = resposta.get('estado_residente')
    estado_residente_id = crud.get_id_by_name(db, models.Estado, 'nome_estado', nome_estado_residente, 'id_estado')

    ##### situacao_conjugal_id #####
    nome_situacao_conjugal = resposta.get("situacao_conjugal")
    situacao_conjugal_id = crud.get_id_by_name(db, models.SituacaoConjugal, 'nome_situacao', nome_situacao_conjugal, 'id_situacao')

    ##### grau_instrucao_id #####
    nome_grau_instrucao = resposta.get("grau_instrucao")
    grau_instrucao_id = crud.get_id_by_name(db, models.GrauInstrucao, 'nome_intrucao', nome_grau_instrucao, 'id_instrucao')

    ##### cor_raca_id #####
    nome_cor_raca = resposta.get("raca")
    cor_raca_id = crud.get_id_by_name(db, models.Raca, 'nome_raca', nome_cor_raca, 'id_raca')

    ##### pais_origem_id #####
    nome_pais_origem = resposta.get('pais_origem')
    pais_origem_id = crud.get_id_by_name(db, models.Paises, 'nome', nome_pais_origem, 'id_pais')

    ##### estado_origem_id #####
    nome_estado_origem = resposta.get('estado_origem')
    estado_origem_id = crud.get_id_by_name(db, models.Estado, 'nome_estado', nome_estado_origem, 'id_estado')

    ##### cancer_hereditario_id #####
    nome_cancer_hereditario = resposta.get('cancer_hereditario')
    cancer_hereditario_id = crud.get_id_by_name(db, models.OpcaoTriviais, 'opcao', nome_cancer_hereditario, 'id_opcao')


    ##### teste_genetico_id #####
    nome_teste_genetico = resposta.get('teste_genetico')
    teste_genetico_id = crud.get_id_by_name(db, models.OpcaoTriviais, 'opcao', nome_teste_genetico, 'id_opcao')

    ##### parentesco_pais_id #####
    nome_parentesco_pais = resposta.get('pais_parentes')
    parentesco_pais_id = crud.get_id_by_name(db, models.ParenteSangue, 'nome', nome_parentesco_pais, 'id_parentesco')

    ##### parentesco_avosm_id #####
    nome_parentesco_avosm = resposta.get('avos_parentes_materno')
    parentesco_avosm_id = crud.get_id_by_name(db, models.ParenteSangue, 'nome', nome_parentesco_avosm, 'id_parentesco')

    ##### parentesco_avosp_id #####
    nome_parentesco_avosp = resposta.get('avos_parentes_paterno')
    parentesco_avosp_id = crud.get_id_by_name(db, models.ParenteSangue, 'nome', nome_parentesco_avosp, 'id_parentesco')

    #### data_nascimento ####
    data_nascimento = resposta.get('data_nascimento')
    if data_nascimento:
        data_nascimento = datetime.fromisoformat(data_nascimento.replace("Z", "+00:00"))
        data_nascimento = data_nascimento.date()
    

    paciente_data = {
                        "quem_respondeu": resposta.get('quem_respondeu'),
                        "paciente": True,
                        "rgh": resposta.get('rgh'),
                        "cpf": resposta.get('cpf'),
                        "nome_paciente": resposta.get('nome_paciente'),
                        "nome_mae": resposta.get('nome_mae'),
                        "genero_id": genero_id,
                        "data_nascimento": data_nascimento,
                        "pais_residente_id": pais_residente_id,
                        "estado_residente_id": estado_residente_id,
                        "cidade_residente": resposta.get('cidade_residente'),
                        "cep_residente": resposta.get('cep_residente'),
                        "situacao_conjugal_id": situacao_conjugal_id,
                        "grau_instrucao_id": grau_instrucao_id,
                        "cor_raca_id": cor_raca_id,
                        "ocupacao": resposta.get('ocupacao'),
                        "tempo_ocupacao": resposta.get('tempo_ocupacao'),
                        "telefone": resposta.get('telefone'),
                        "email": resposta.get('email'),
                        "idade": resposta.get('idade'),
                        "pais_origem_id": pais_origem_id,
                        "cidade_origem": resposta.get('cidade_origem'),
                        "estado_origem_id": estado_origem_id,
                        "adotado": resposta.get('adotado'),
                        "cancer": resposta.get('teve_cancer'),
                        "cancer_hereditario_id": cancer_hereditario_id,
                        "teste_genetico_id": teste_genetico_id,
                        "informacoes_corretas": resposta.get('informacoes_corretas'),
                        "parentesco_pais_id": parentesco_pais_id,
                        "parentesco_avosm_id": parentesco_avosm_id,
                        "parentesco_avosp_id": parentesco_avosp_id
                    }
    
    paciente_create = schemas.PacienteCreate(**paciente_data)
    paciente = create_paciente(paciente_create, db)

    
    #### PacienteDoenca ####
    tipo_doencas = resposta.get('diagnosticos')
    if tipo_doencas:
        for doenca in tipo_doencas:
            tipo_doencas_id = crud.get_id_by_name(db, models.TipoDoencas, 'nome_doenca', doenca, 'id_doenca')
            paciente_doenca_data = {
            "id_paciente": paciente.id_paciente,
            "id_doenca": tipo_doencas_id,
            "doenca_outro": resposta.get('outroDiagnostico')
            }
            paciente_doenca_create = schemas.PacienteDoencaCreate(**paciente_doenca_data)
            doenca = create_paciente_doenca(paciente_doenca_create, db)

    #### PacienteCancer ####
    if resposta.get('teve_cancer'):
        tipo_cancer = resposta.get('cancers_que_teve_paciente')
        idades = resposta.get('idade_inicio_cancers_paciente')
        for cancer, idade in zip(tipo_cancer, idades):
            tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
            paciente_cancer_data = {
            "id_paciente": paciente.id_paciente,
            "id_cancer": tipo_cancer_id,
            "idade": int(idade)
            }
            paciente_cancer_create = schemas.PacienteCancerCreate(**paciente_cancer_data)
            cancer = create_paciente_cancer(paciente_cancer_create, db)

    #### PacienteLesao ####
    tipo_lesao = resposta.get('lesao_atual')
    if tipo_lesao:
        idade = resposta.get('idade_inicio_lesao')
        if idade is not None:
            idade = int(idade)
        for lesao in tipo_lesao:
            tipo_lesao_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', lesao, 'id_cancer')
            paciente_lesao_data = {
            "id_paciente": paciente.id_paciente,
            "id_lesao": tipo_lesao_id,
            "idade": idade
            }
            paciente_lesao_create = schemas.PacienteLesaoCreate(**paciente_lesao_data)
            lesao = create_paciente_lesao(paciente_lesao_create, db)

    #### Parente ####
    pai_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "pai", 'id_parentesco')
    mae_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "mae", 'id_parentesco')
    avo_paterno_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "avô paterno", 'id_parentesco')
    avo_paterna_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "avó paterna", 'id_parentesco')
    avo_materno_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "avô materno", 'id_parentesco')
    avo_materna_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "avó materna", 'id_parentesco')
    filho_id = crud.get_id_by_name(db, models.GrauParentesco, 'nome', "filho", 'id_parentesco')

    parentes_list_id = [pai_id, mae_id, avo_paterno_id, avo_paterna_id, avo_materno_id, avo_materna_id] 
    # gerando quantidade de filhos correta
    qtd_filhos = int(resposta.get('quantidade_filho_cancer'))
    if qtd_filhos > 0:
        for i in range(qtd_filhos):
            parentes_list_id.append(filho_id)

    # Lista para salvar tupla de parente_id e parentesco_id
    parentes_parentesco = []

    for parentesco_id in parentes_list_id:
        parente_data = {
            "id_paciente": paciente.id_paciente,
            "id_parentesco": parentesco_id
        }
        parente_create = schemas.ParenteCreate(**parente_data)
        parente = create_parente(parente_create, db)

        # salvando id do parente e id do parentesco juntos
        parente_id = parente.id_parente
        parentes_parentesco.append((parentesco_id, parente_id))

    
    #### ParenteDoenca ####
    tipo_doencas = resposta.get('familia_diagnosticos')
    if tipo_doencas:
        for doenca in tipo_doencas:
            tipo_doencas_id = crud.get_id_by_name(db, models.TipoDoencas, 'nome_doenca', doenca, 'id_doenca')
            parente_doenca_data = {
            "id_paciente": paciente.id_paciente,
            "id_doenca_familia": tipo_doencas_id,
            "doenca_familia_outro": resposta.get('familia_diagnostico_outro')
            }
            parente_doenca_create = schemas.ParenteDoencaCreate(**parente_doenca_data)
            parente_doenca = create_parente_doenca(parente_doenca_create, db)

    #### ParenteCancer ####
    filhos_adiconados = 0
    for parentesco_id, parente_id in parentes_parentesco:
        # Se pai teve cancer:
        if resposta.get("opcao_pai_cancer") == "Sim" and parentesco_id == pai_id:
            tipo_cancer_list = resposta.get('pai_cancer')
            idades = resposta.get('idade_inicio_cancers_pai')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)

        # Se mae teve cancer:
        if resposta.get("opcao_mae_cancer") == "Sim" and parentesco_id == mae_id:
            tipo_cancer_list = resposta.get('mae_cancer')
            idades = resposta.get('idade_inicio_cancers_mae')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)

        # Se avo paterno teve cancer:
        if resposta.get("opcao_avo_paterno_cancer") == "Sim" and parentesco_id == avo_paterno_id:
            tipo_cancer_list = resposta.get('avo_paterno_cancer')
            idades = resposta.get('idade_inicio_cancers_avo_paterno')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)

        # Se avo paterna teve cancer:
        if resposta.get("opcao_avo_paterna_cancer") == "Sim" and parentesco_id == avo_paterna_id:
            tipo_cancer_list = resposta.get('avo_paterna_cancer')
            idades = resposta.get('idade_inicio_cancers_avo_paterna')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)
        
        # Se avo materno teve cancer:
        if resposta.get("opcao_avo_materno_cancer") == "Sim" and parentesco_id == avo_materno_id:
            tipo_cancer_list = resposta.get('avo_materno_cancer')
            idades = resposta.get('idade_inicio_cancers_avo_materno')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)

        
        # Se avo materna teve cancer:
        if resposta.get("opcao_avo_materna_cancer") == "Sim" and parentesco_id == avo_materna_id:
            tipo_cancer_list = resposta.get('avo_materna_cancer')
            idades = resposta.get('idade_inicio_cancers_avo_materna')
            if not idades:
                 idades = [None] * len(tipo_cancer_list)
            for cancer, idade in zip(tipo_cancer_list, idades):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)

        # Se filho teve cancer:
        if resposta.get("algum_filho_tem_ou_teve_cancer") and parentesco_id == filho_id:
            tipo_cancer_list = resposta.get('tipo_cancer_filho')
            idades = resposta.get('idade_inicio_cancers_filho')
            # tatando caso quando a lista idades é uma lista vazia
            if not idades:
                idades = [[None] for _ in range(len(tipo_cancer_list))]
            for cancer, idade in zip(tipo_cancer_list[filhos_adiconados], idades[filhos_adiconados]):
                tipo_cancer_id = crud.get_id_by_name(db, models.TipoCancer, 'nome', cancer, 'id_cancer')
                if idade is not None:
                    idade = int(idade)
                parente_cancer_data = {
                "id_parente": parente_id,
                "id_cancer": tipo_cancer_id,
                "idade": idade
                }
                parente_cancer_create = schemas.ParenteCancerCreate(**parente_cancer_data)
                parente_cancer = create_parente_cancer(parente_cancer_create, db)
            filhos_adiconados += 1   
    
    return {"message": "Dados recebidos com sucesso!"}

@app.post("/submit-form/")
async def submit_form_data(resposta: dict, db : Session = Depends(get_db)):
    return {"message": "Dados recebidos com sucesso!"}