# pylint:disable=missing-docstring
import random
from functools import partial
from pathlib import Path

import mysql.connector
from dotenv import dotenv_values
from tqdm import tqdm
from funcs_aux import profissoes, nomes_unissex, cidades_ficticias, data_e_idade_aleatoria


def run_db_query(connection, query, args=None):
    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(query, args)
        for result in cursor:
            print(result)


def run_db_query_insert(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args)


def run_db_query_index(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args)
        list_result = []
        for result in cursor:
            list_result.append(result[0])
        return list_result


def main():
    env_path = Path(__file__).parent / ".env"
    env = dict(dotenv_values(env_path))

    connection = mysql.connector.connect(
        host=env.get('DB_HOST'),
        user=env.get('DB_USER'),
        password=env.get('DB_PASSWORD'),
        database=env.get('DB_DATABASE_NAME'),
    )

    db_insert = partial(run_db_query_insert, connection)
    db_index = partial(run_db_query_index, connection)

    # Simulação de dados
    for _ in tqdm(range(1000)):
        # Simulação Tabela Paciente
        quem_respondeu = random.choice(["Pelo próprio", "Outro"])
        paciente = random.choice([True, False])
        rgh = random.randint(10000, 99999)
        sorteia_cpf = str(random.randint(10000000000, 99999999999))
        cpf = f"{sorteia_cpf[:3]}.{sorteia_cpf[3:6]}.{sorteia_cpf[6:9]}-{sorteia_cpf[9:]}"
        nome_paciente = random.choice(nomes_unissex)
        nome_mae = random.choice(nomes_unissex)
        genero_id = random.choice(db_index("SELECT * FROM TipoGenero"))
        data_nascimento, idade = data_e_idade_aleatoria()
        pais_residente_id = random.choice(
            db_index("SELECT * FROM Paises"))  # TO DO: Ter mais Brasil?
        cidade_residente = random.choice(
            cidades_ficticias)  # TO DO: Problemático cidades fictícias?
        if pais_residente_id == 35:
            estado_residente_id = random.choice(
                db_index("SELECT * FROM Estado"))
        else:
            estado_residente_id = "NULL"
        sorteia_cep_residente = str(random.randint(10000000, 99999999))
        cep_residente = f"{sorteia_cep_residente[:5]}-{sorteia_cep_residente[5:]}"
        situacao_conjugal_id = random.choice(
            db_index("SELECT * FROM SituacaoConjugal"))  # TO DO: Problemático?
        grau_instrucao_id = random.choice(
            db_index("SELECT * FROM GrauInstrucao"))  # TO DO: Problemático?
        cor_raca_id = random.choice(
            db_index("SELECT * FROM Raca"))  # TO DO: Problemático?
        ocupacao = random.choice(profissoes)
        # TO DO: esses valores foram adotados para não ter discrepâncias com
        # as idades, problemático ?
        if idade < 40 and idade > 25:
            tempo_ocupacao = random.randint(1, 7)
        elif idade <= 25 and idade > 20:
            tempo_ocupacao = random.randint(1, 3)
        elif idade <= 20 and idade >= 18:
            tempo_ocupacao = 1
        else:
            tempo_ocupacao = random.randint(1, 23)
        telefone = str(random.randint(10000000000, 99999999999))
        email = nome_paciente + '@gmail.com'
        pais_origem_id = random.choice(
            db_index("SELECT * FROM Paises"))  # TO DO: Ter mais Brasil?
        cidade_origem = random.choice(
            cidades_ficticias)  # TO DO: Problemático cidades fictícias?
        if pais_origem_id == 35:
            estado_origem_id = random.choice(db_index("SELECT * FROM Estado"))
        else:
            estado_origem_id = 'NULL'
        adotado = False
        cancer = random.choice([True, False])
        cancer_hereditario_id = random.choice(
            db_index("SELECT * FROM OpcaoTriviais"))
        teste_genetico_id = random.choice(
            db_index("SELECT * FROM OpcaoTriviais"))
        informacoes_corretas = True
        parentesco_pais_id = random.choice(
            db_index("SELECT * FROM ParenteSangue"))
        parentesco_avosm_id = random.choice(
            db_index("SELECT * FROM ParenteSangue"))
        parentesco_avosp_id = random.choice(
            db_index("SELECT * FROM ParenteSangue"))

        # simula tabela paciente
        insert_paciente = f"""INSERT INTO `Paciente` (
                            `quem_respondeu`  ,
                            `paciente`  ,
                            `rgh`  ,
                            `cpf`  ,
                            `nome_paciente`  ,
                            `nome_mae`  ,
                            `genero_id`  ,
                            `data_nascimento`  ,
                            `pais_residente_id`  ,
                            `cidade_residente`  ,
                            `estado_residente_id`  ,
                            `cep_residente`  ,
                            `situacao_conjugal_id`  ,
                            `grau_instrucao_id`  ,
                            `cor_raca_id`  ,
                            `ocupacao`  ,
                            `tempo_ocupacao`  ,
                            `telefone`  ,
                            `email`  ,
                            `idade`  ,
                            `pais_origem_id`  ,
                            `cidade_origem`  ,
                            `estado_origem_id`  ,
                            `adotado`,
                            `cancer`,
                            `cancer_hereditario_id`,
                            `teste_genetico_id`  ,
                            `informacoes_corretas`  ,
                            `parentesco_pais_id`  ,
                            `parentesco_avosm_id`  ,
                            `parentesco_avosp_id`  
                        )                
                        VALUES (
                            '{quem_respondeu}', 
                            {paciente}, 
                            {rgh}, 
                            '{cpf}', 
                            '{nome_paciente}' , 
                            '{nome_mae}' , 
                            {genero_id} , 
                            '{data_nascimento}', 
                            {pais_residente_id} , 
                            '{cidade_residente}', 
                            {estado_residente_id} , 
                            {cep_residente} , 
                            {situacao_conjugal_id} , 
                            {grau_instrucao_id} , 
                            {cor_raca_id} , 
                            '{ocupacao}' , 
                            {tempo_ocupacao} , 
                            {telefone} , 
                            '{email}' , 
                            {idade} , 
                            {pais_origem_id} , 
                            '{cidade_origem}' , 
                            {estado_origem_id} , 
                            {adotado} , 
                            {cancer} , 
                            {cancer_hereditario_id} , 
                            {teste_genetico_id} , 
                            {informacoes_corretas} , 
                            {parentesco_pais_id} , 
                            {parentesco_avosm_id} , 
                            {parentesco_avosp_id}
                        )"""
        db_insert(insert_paciente)

        id_paciente = db_index("SELECT LAST_INSERT_ID()")[0]

        # simula tabela PacienteDoenca
        lista_id_doenca = random.sample(
            db_index("SELECT * FROM TipoDoencas"),
            random.randint(0, 3))  # TO DO: Considera no máximo 3 doenças?

        # Para evitar duplicatas na tabela PacienteDoenca, verifique se
        # o registro já existe antes de inseri-lo.
        for id_doenca in lista_id_doenca:
            # Verifique se o registro já existe
            if not db_index(
                    "SELECT * FROM PacienteDoenca WHERE id_paciente = %s AND id_doenca = %s",
                (id_paciente, id_doenca)):
                if id_doenca == 10:
                    doenca_outro = "Doença Psicológica"
                else:
                    doenca_outro = None

                # Insira o registro apenas se não existir
                insert_paciente_doenca = """INSERT INTO `PacienteDoenca` (
                                                `id_paciente`,
                                                `id_doenca`,
                                                `doenca_outro`
                                            )                
                                            VALUES (%s, %s, %s)"""
                db_insert(insert_paciente_doenca,
                          (id_paciente, id_doenca, doenca_outro))

        # simula tabela PacienteCancer
        if cancer:
            lista_id_cancer = random.sample(
                db_index("SELECT * FROM TipoCancer"),
                random.randint(1, 3))  # TO DO: Considera no máximo 3 canceres?
            for id_cancer in lista_id_cancer:
                if not db_index(
                        "SELECT * FROM PacienteCancer WHERE id_paciente = %s AND id_cancer = %s",
                    (id_paciente, id_cancer)):
                    if id_cancer == 10:
                        cancer_outro = "Sinovial"
                    else:
                        cancer_outro = None

                    if len(lista_id_cancer) > 0:
                        idade_inicio_cancer = random.randint(
                            idade - 3, idade - 1)
                    else:
                        idade_inicio_cancer = None

                    # Insira o registro apenas se não existir
                    insert_paciente_cancer = """INSERT INTO `PacienteCancer` (
                                                    `id_paciente`,
                                                    `id_cancer`,
                                                    `idade`,
                                                    `cancer_outro`
                                                )                
                                                VALUES (%s, %s, %s, %s)"""
                    db_insert(insert_paciente_cancer,
                              (id_paciente, id_cancer, idade_inicio_cancer,
                               cancer_outro))

        # simula tabela ResultadoGenetico
        id_tipo_procedimento = random.choice(
            db_index("SELECT * FROM TipoProcedimento"))
        id_gene = random.choice(db_index("SELECT * FROM Gene"))
        resultado = random.choice([True, False])
        # Insira o registro apenas se não existir
        insert_resultado_genetico = """INSERT INTO `ResultadoGenetico` (
                                        `id_paciente`,
                                        `id_gene`,
                                        `id_tipo_proc`,
                                        `resultado`
                                    )                
                                    VALUES (%s, %s, %s, %s)"""
        db_insert(insert_resultado_genetico,
                  (id_paciente, id_gene, id_tipo_procedimento, resultado))

        # simula tabela Parente
        lista_id_parentesco = [
            3, 4, 5, 6, 7, 8
        ]  # TO DO: todos tem informações dos pais e avós

        for id_parentesco in lista_id_parentesco:
            nome_parente = random.choice(nomes_unissex)
            insert_parente = """INSERT INTO `Parente` (
                                            `id_paciente`,
                                            `id_parentesco`,
                                            `nome`
                                        )                
                                        VALUES (%s, %s, %s)"""
            db_insert(insert_parente,
                      (id_paciente, id_parentesco, nome_parente))

            id_parente = db_index("SELECT LAST_INSERT_ID()")[0]

            # simula tabela ParenteDoenca
            lista_id_doenca = random.sample(
                db_index("SELECT * FROM TipoDoencas"),
                random.randint(0, 3))  # TO DO: Considera no máximo 3 doenças?

            # Para evitar duplicatas na tabela ParenteDoenca, verifique se
            # o registro já existe antes de inseri-lo.
            for id_doenca in lista_id_doenca:
                # Verifique se o registro já existe
                if not db_index(
                        "SELECT * FROM ParenteDoenca WHERE id_parente = %s AND id_doenca = %s",
                    (id_parente, id_doenca)):
                    if id_doenca == 10:
                        doenca_outro = "Doença Psicológica"
                    else:
                        doenca_outro = None

                    # Insira o registro apenas se não existir
                    insert_parente_doenca = """INSERT INTO `ParenteDoenca` (
                                                    `id_parente`,
                                                    `id_doenca`,
                                                    `doenca_outro`
                                                )                
                                                VALUES (%s, %s, %s)"""
                    db_insert(insert_parente_doenca,
                              (id_parente, id_doenca, doenca_outro))

            lista_id_cancer = random.sample(
                db_index("SELECT * FROM TipoCancer"),
                random.randint(0, 3))  # TO DO: Considera no máximo 3 canceres?
            for id_cancer in lista_id_cancer:
                if not db_index(
                        "SELECT * FROM ParenteCancer WHERE id_parente = %s AND id_cancer = %s",
                    (id_parente, id_cancer)):
                    if id_cancer == 10:
                        cancer_outro = "Sinovial"
                    else:
                        cancer_outro = None

                    if len(lista_id_cancer) > 0 and id_cancer != -1:
                        idade_inicio_cancer = random.randint(30, 70)
                    else:
                        idade_inicio_cancer = None

                    # Insira o registro apenas se não existir
                    insert_parente_cancer = """INSERT INTO `ParenteCancer` (
                                                    `id_parente`,
                                                    `id_cancer`,
                                                    `idade`,
                                                    `cancer_outro`
                                                )                
                                                VALUES (%s, %s, %s, %s)"""
                    db_insert(insert_parente_cancer,
                              (id_parente, id_cancer, idade_inicio_cancer,
                               cancer_outro))

            if id_parentesco in [5, 6, 7, 8]:
                id_origem = random.choice(db_index("SELECT * FROM Origem"))

                # Insira o registro apenas se não existir
                insert_origem_parente = """INSERT INTO `OrigemParente` (
                                                `id_origem`,
                                                `id_parente`
                                            )                
                                            VALUES (%s, %s)"""
                db_insert(insert_origem_parente, (id_origem, id_parente))

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
