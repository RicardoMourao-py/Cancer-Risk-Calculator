# pylint:disable=missing-docstring
from datetime import datetime, timedelta
import random

profissoes = [
    "Engenheiro",
    "Médico",
    "Professor",
    "Advogado",
    "Programador",
    "Designer",
    "Enfermeiro",
    "Arquiteto",
    "Contador",
    "Artista",
    "Cientista de Dados",
    "Analista de Sistemas",
    "Consultor Financeiro",
    "Gerente de Projetos",
    "Empresário",
    "Estudante",
    "Jornalista",
    "Psicólogo",
    "Farmacêutico",
    "Chef de Cozinha",
]

nomes_unissex = [
    "Alex",
    "Taylor",
    "Jordan",
    "Casey",
    "Morgan",
    "Jamie",
    "Jesse",
    "Avery",
    "Cameron",
    "Peyton",
]

cidades_ficticias = [
    "Nova Esperança",
    "Cidade dos Sonhos",
    "Vale Verde",
    "Monte Celestial",
    "Rio da Aurora",
    "Praia da Serenidade",
    "Aldeia dos Ventos",
    "Montanha da Harmonia",
    "Floresta Encantada",
    "Ilha da Fantasia",
]


def data_e_idade_aleatoria():
    # Define um intervalo de idade (por exemplo, de 18 a 80 anos)
    idade_minima = 18
    idade_maxima = 90

    # Obtém a data atual
    data_atual = datetime.now()

    # Calcula a data mínima de nascimento (idade máxima)
    data_minima = data_atual - timedelta(days=idade_maxima * 365)

    # Calcula a data máxima de nascimento (idade mínima)
    data_maxima = data_atual - timedelta(days=idade_minima * 365)

    # Gera uma data de nascimento aleatória dentro do intervalo definido
    data_nascimento = data_minima + timedelta(
        days=random.randint(0, (data_maxima - data_minima).days))

    # Calcula a idade atual com base na data de nascimento
    idade = data_atual.year - data_nascimento.year \
        - ((data_atual.month, data_atual.day) \
            < (data_nascimento.month, data_nascimento.day))

    return data_nascimento.date(), idade
