### Prediction Application
Diretório responsável por desenvolver o modelo preditor que está inserido à aplicação do formulário.

#### Data
Diretório onde estão os dados simulados que serão treinados no modelo de _RandomForestClassifier_.

#### Models 
Diretório onde está o modelo _classifier.pkl_ devidamente treinado e que será utilizado na predição dos resultados de teste genéticos.

#### Training

Diretório com o arquivo `model_functions.py` que contém funcões utilizadas no arquivo `exploring_model.ipynb` o qual foi utilizado no intuito de explorar a modelagem dos dados simulados com técnicas de _machine_learning_ e avaliação das métricas do modelo utilizado (_RandomForestClassifier_).

#### Outros arquivos

`main.py`, `mock_model.py` e `preditor.py` são os arquivos responsáveis por, de forma integrada, subir a rota de predição em _FastApi_ que será utilizada também no preenchimento do formulário . 
