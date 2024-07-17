# Dicionário de Dados



### Tabela **paciente**
* Contém informação pessoal e clínica dos pacientes

| Coluna                | Descrição                                                               |
|-----------------------|-------------------------------------------------------------------------|
| id_paciente           | identificador numérico paciente                                         |
| quem_respondeu        | quem respondeu o questionário (paciente ou outra pessoa)                |
| paciente              | nome do paciente                                                        |
| rgh                   | registro geral do hospital                                              |
| cpf                   | CPF do paciente                                                         |
| nome_paciente         | nome paciente                                                           |
| nome_mae              | nome da mãe do paciente                                                 |
| genero_id             | gênero do paciente, chave estrangeira tabela TipoGenero                 |
| data_nascimento       | data nascimento do paciente                                             |
| pais_residente_id     | identificador país de residência do paciente, chave estrangeira Tabela Paises |
| cidade_residente      | cidade de residência do paciente                                        |
| cep_residente         | CEP de residência do paciente                                           |
| situacao_conjugal_id  | identificador situação conjugal paciente, chave estrangeira Tabela SituacaoConjugal |
| grau_instrucao_id     | identificador grau instrução paciente, chave estrangeira Tabela GrauInstrucao |
| cor_raca_id           | identificador raça paciente, chave estrangeira Tabela Raca              |
| ocupacao              | ocupação que o paciente ocupou por mais tempo                           |
| tempo_ocupacao        | tempo relativo à ocupação na linha anterior                             |
| telefone              | telefone do paciente                                                    |
| email                 | email do paciente                                                       |
| idade                 | idade do paciente                                                       |
| pais_origem_id        | identificador país de origem do paciente, chave estrangeira Tabela Paises |
| estado_origem_id      | identificador raça paciente, chave estrangeira Tabela Estado            |
| adotado               | se o paciente é ou não adotado                                          |
| diagnostico_outro     | outro diagnóstico não especificado no formulário                        |
| cancer                | considera dois valores se a pessoa tem ou não câncer                    |
| diagnostico_parente_outro | outro diagnóstico do parente não especificado no formulário          |
| cancer_hereditario_id | identificador possibilidade de câncer hereditário do paciente, chave estrangeira Tabela OpcaoTriviais |
| teste_genetico_id     | identificador possibilidade de ter feito teste genético do paciente, chave estrangeira Tabela OpcaoTriviais |
| informacoes_corretas  | opção (Sim ou não) se as informações fornecidas pelo paciente estão corretas |
| parentesco_pais_id    | identificador do parentesco dos pais do paciente, chave estrangeira Tabela PaisParentes |


### Tabela **grauinstrucao**
* Lista os possíveis graus de instrução formal
* Conteúdo fixo, listando desde "Analfabeto/pré-primário", "Ensino primário/fundamental", "Ensino médio/segundo grau/normal/antigo científico/técnico", "Ensino superior incompleto", "Ensino superior completo", "Pós-graduação/mestrado/especialização/residência", "Doutorado e pós-doutorado" e "Prefiro não responder"

| Coluna        | Descrição                                          |
|---------------|----------------------------------------------------|
| id_instrucao  | identificador numérico grau de instrução, chave primária |
| nome          | nome deste grau de instrução                       |


### Tabela **situacaoconjugal**
* Lista os possíveis graus de situação conjugal
* Conteúdo fixo: "solteiro(a)", "casado(a)/companheiro(a)/amigado(a)", "separado(a)/divorciado(a)" e "viúvo(a)".

| Coluna        | Descrição                                          |
|---------------|----------------------------------------------------|
| id_situacao   | identificador numérico situação conjugal, chave primária |
| nome_situacao | nome desta situação conjugal                       |


### Tabela **opcaotriviais**
* Lista os possíveis opções de resposta
* Conteúdo fixo, listando desde "Não", "Sim" e "Não sei".

| Coluna    | Descrição                                   |
|-----------|---------------------------------------------|
| id_opcao  | identificador numérico opções triviais, chave primária |
| opcao     | nome desta opção                            |


### Tabela **paises**
* Lista os possíveis países
* Conteúdo fixo, uma lista de 259 países.

| Coluna  | Descrição                             |
|---------|---------------------------------------|
| id_pais | identificador numérico de países, chave primária |
| nome    | nome deste país                       |


### Tabela **paisparentes**
* Lista os possíveis graus de parentesco entre pais
* Conteúdo fixo, listando desde "Não são da mesma família", "São parentes/primos" e "Não são da mesma família".

| Coluna         | Descrição                                   |
|----------------|---------------------------------------------|
| id_parentesco  | identificador numérico parentesco dos pais, chave primária |
| nome           | nome deste grau de parentesco               |


### Tabela **origem**
* Lista os possíveis origens
* Conteúdo fixo, listando alguns tipos de origens

| Coluna       | Descrição                        |
|--------------|----------------------------------|
| id_origem    | identificador numérico origem, chave primária |
| nome_origem  | nome desta origem                |


### Tabela **origemparente**
* Lista os possíveis origens do parente
* Conteúdo fixo, listando a origem de cada parente daquele paciente

| Coluna     | Descrição                                           |
|------------|-----------------------------------------------------|
| id_origem  | identificador numérico origem, chave primária ,chave estrangeira Tabela Origem |
| id_parente | identificador numérico parente, chave primária ,chave estrangeira Tabela Parente |


### Tabela **grauparentesco**
* Lista os possíveis graus de parentesco
* Conteúdo fixo, listando os graus de Parentesco existentes ("filho", "pai", "mãe", "tio paterno", dentre outros)

| Coluna         | Descrição                                   |
|----------------|---------------------------------------------|
| id_parentesco  | identificador numérico parentesco, chave primária |
| nome           | nome deste grau de instrução                |


### Tabela **parente**
* Lista os parentes de um paciente
* Conteúdo fixo, listando todos os parentes pelo seu identificador

| Coluna         | Descrição                                   |
|----------------|---------------------------------------------|
| id_parente     | identificador numérico parente, chave primária |
| id_paciente    | identificador numérico paciente ,chave estrangeira Tabela Paciente |
| id_parentesco  | identificador numérico parentesco ,chave estrangeira Tabela GrauParentesco |
| nome           | nome do parente                             |


### Tabela **raca**
* Lista as possíveis raças
* Conteúdo fixo, listando desde "Branco/pele clara/clara", "Parda/morena/mulata/mestiça", "Preta/negra/africana/escura", "Amarela/oriental/asiática", "Indígena" e "Prefiro não responder"

| Coluna    | Descrição                      |
|-----------|--------------------------------|
| id_raca   | identificador numérico raça, chave primária |
| nome_raca | nome desta raça               |


### Tabela **cancerparente**
* Lista os parentes e tipos de câncer de cada parente do paciente
* Conteúdo fixo, listando o identificador do parente e o identificador do seu câncer

| Coluna     | Descrição                                           |
|------------|-----------------------------------------------------|
| id_parente | identificador numérico parente, chave primária ,chave estrangeira Tabela Parente |
| id_cancer  | identificador numérico tipo de câncer, chave primária ,chave estrangeira Tabela TipoCancer |
| idade      | idade a qual surgiu o câncer                       |


### Tabela **tipocancer**
* Lista os possíveis tipos de câncer
* Conteúdo fixo, listando 15 tipos de câncer existentes

| Coluna    | Descrição                          |
|-----------|------------------------------------|
| id_cancer | identificador numérico tipo de câncer, chave primária |
| nome      | nome deste tipo de câncer          |


### Tabela **pacientecancer**
* Lista os pacientes, tipos de câncer e idade de início do câncer
* Conteúdo fixo, listando os tipos de câncer de um determinado paciente

| Coluna      | Descrição                                           |
|-------------|-----------------------------------------------------|
| id_paciente | identificador numérico paciente, chave primária ,chave estrangeira Tabela Paciente |
| id_cancer   | identificador numérico tipo de câncer, chave primária ,chave estrangeira Tabela TipoCancer |
| idade       | idade que começou o câncer referido pelo identificador |


### Tabela **estado**
* Lista os possíveis estados brasileiros
* Conteúdo fixo, listando todos os estados brasileiros

| Coluna      | Descrição                           |
|-------------|-------------------------------------|
| id_estado   | identificador numérico estado, chave primária |
| nome_estado | nome deste estado                   |


### Tabela **parentedoenca**
* Lista os parentes e tipos de doenças para cada paciente
* Conteúdo fixo, listando as doenças de um determinado paciente

| Coluna     | Descrição                                           |
|------------|-----------------------------------------------------|
| id_parente | identificador numérico parente, chave primária ,chave estrangeira Tabela Parente |
| id_doenca  | identificador numérico tipo de doença, chave primária ,chave estrangeira Tabela TipoDoencas |

### Tabela **tipodoencas**
* Lista os possíveis tipos de doenças
* Conteúdo fixo, listando 9 tipos de doenças

| Coluna     | Descrição                            |
|------------|--------------------------------------|
| id_doenca  | identificador numérico da doença, chave primária |
| nome_doenca | nome desta doença                   |


### Tabela **tipogenero**
* Lista os possíveis gêneros
* Conteúdo fixo, listando desde "Masculino", "Feminino" e "Outros"

| Coluna     | Descrição                           |
|------------|-------------------------------------|
| id_genero  | identificador numérico tipo de gênero, chave primária |
| nome       | nome deste tipo de gênero           |

### Tabela **pacientedoenca**
* Lista as doenças de um determinado paciente
* Conteúdo fixo, listando as doenças de um determinado paciente

| Coluna      | Descrição                                           |
|-------------|-----------------------------------------------------|
| id_paciente | identificador numérico paciente, chave primária ,chave estrangeira Tabela Paciente |
| id_doenca   | identificador numérico tipo de doença , chave primária ,chave estrangeira Tabela TipoDoencas |
