# -*- coding: utf-8 -*-

# 1. Library imports
# import sys
import os
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel # pylint: disable=no-name-in-module
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from .mock_model import MockModel
from typing import Optional

models_path = Path(Path(os.getcwd()) / 'app' / 'models')  
pickle_file_path = models_path / "classifier.pkl" 

class Paciente(BaseModel):
    """Classe que descreve as informações de um paciente."""
    vc_tem_lesao_atualmente: Optional[int]
    idade_inicio_problema_atual: Optional[int]
    onde_lesao: Optional[int]
    tipo_cancer_paciente: Optional[int]
    algum_filho_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_filho: Optional[int]
    pai_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_pai: Optional[int]
    mae_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_mae: Optional[int]
    avo_paterno_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_avo_paterno: Optional[int]
    avo_paterna_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_avo_paterna: Optional[int]
    avo_materno_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_avo_materno: Optional[int]
    avo_materna_tem_ou_teve_cancer: Optional[int]
    tipo_cancer_avo_materna: Optional[int]


# 2. Create the app object
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

# 3. Index route, opens automatically on http://127.0.0.1:8080
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 3. Expose the prediction functionality, make a prediction from the passed
@app.post('/predict')
def predict_teste_genetico(data: Paciente):
    model=MockModel()

    classifier = model.load(pickle_file_path)
    data = data.dict()
    list_data=[data[key] for key in data.keys()]
    input_array=np.array([list_data])

    prediction = classifier.predict([list_data])
    probabilidades_teste_positivo=classifier.predict_proba(input_array)[0][1]
    probabilidades_teste_negativo=1-probabilidades_teste_positivo

    if prediction[0]== 1:
        prediction = "Resultado positivo para teste genético:Indica ocorrência de algum tipo de mutação"
    else:
        prediction = "Resultado negativo para teste genético:Não indica ocorrência de mutação"
    return {
        'prediction': prediction,
        'predictionProba_positivo':round(probabilidades_teste_positivo,2),
        'predictionProba_negativo':round(probabilidades_teste_negativo,2)    
    }