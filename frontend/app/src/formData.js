import { useState, useEffect } from 'react';

export const initialFormData = {
    quem_respondeu: '',
    paciente: false,
    rgh: '',
    cpf: '',
    nome_paciente: '',
    nome_mae: '',
    genero: '',
    data_nascimento: new Date(),
    pais_residente: '',
    estado_residente:'',
    cidade_residente: '',
    cep_residente: '',
    situacao_conjugal: '',
    grau_instrucao: '',
    raca: '',
    ocupacao: '',
    tempo_ocupacao: 0,
    telefone: '',
    email: '',
    idade: 0, 
    pais_origem: '',  // novo campo
    cidade_origem: '',  // novo campo
    estado_origem: '',  // novo campo
    adotado: false,
    diagnosticos: [],
    outroDiagnostico: '', // novo campo
    lesao_atual: [],
    idade_inicio_lesao: 0,
    opcoes_tumor:'',
    teve_cancer:false,
    cancers_que_teve_paciente:[],
    idade_inicio_cancers_paciente:[],
    familia_diagnosticos:[],
    familia_diagnostico_outro:'',  // novo campo
    cancer_hereditario: '',  // novo campo
    teste_genetico: '',  // novo campo
    opcao_pai_cancer: '',
    pai_cancer: [],
    idade_inicio_cancers_pai: [],
    opcao_mae_cancer: '',
    mae_cancer: [],
    idade_inicio_cancers_mae: [],
    pais_parentes: '',

    opcao_avo_paterno_cancer: '',
    avo_paterno_cancer: [],
    idade_inicio_cancers_avo_paterno: [],
    origem_avo_paterno: '',

    opcao_avo_paterna_cancer: '',
    avo_paterna_cancer: [],
    idade_inicio_cancers_avo_paterna: [],
    origem_avo_paterna: '',
    avos_parentes_paterno: '',


    opcao_avo_materno_cancer: '',
    avo_materno_cancer: [],
    idade_inicio_cancers_avo_materno: [],
    origem_avo_materno: '',

    opcao_avo_materna_cancer: '',
    avo_materna_cancer: [],
    idade_inicio_cancers_avo_materna: [],
    origem_avo_materna: '',
    avos_parentes_materno: '',

    informacoes_corretas: false, // novo campo

    algum_filho_tem_ou_teve_cancer: '',
    quantidade_filho_cancer: 0,
    tipo_cancer_filho: [],
    idade_inicio_cancers_filho: []
};

export const useFormData = () => {
    const [formData, setformData] = useState(() => {
        const savedFormData = JSON.parse(localStorage.getItem('formData'));
        return savedFormData || initialFormData;
    });

    useEffect(() => {
        localStorage.setItem('formData', JSON.stringify(formData));
    }, [formData]);

    return { formData, setformData };
};