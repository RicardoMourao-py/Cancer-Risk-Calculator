import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'
import api from './api';
import { Link } from 'react-router-dom'; // Importe o Link para navegação entre rotas
import {  Button } from '@mui/material';

import {renderOptionButtonGroupDiv,renderTable} from './ButtonComponents';
import {GenericInput,GenericSelect,handleCheckboxChange,
generateCheckboxes, handleCheckboxChange2} from './FormInputs';
import * as consts from './consts';
import logo from './logo.png'
import './App.css';
import { useFormData } from './formData';

const App = () => {

  const { formData, setformData } = useFormData();
  
  const [formParente, setformParente] = useState({

  });


  const navigate = useNavigate();

  const [generos, setGeneros] = useState([]);
  
  const fetchGeneros = async () => {
      const response = await api.get('/genero/');
      setGeneros(response.data);
    };
  
  const [paises, setPaises] = useState([]);
  const fetchPaises = async () => {
      const response = await api.get('/paises/');
      setPaises(response.data);
    };
  
  const [estados, setEstados] = useState([]);
  const fetchEstados = async () => {
      const response = await api.get('/estado/');
      setEstados(response.data);
    };

  const [situacao_conjugal, setsituacao_conjugal] = useState([]);
  const fetchsituacao_conjugal = async () => {
      const response = await api.get('/situacao_conjugal/');
      setsituacao_conjugal(response.data);
    };  
  
  const [grau_instrucao, setgrau_instrucao] = useState([]);
  const fetchgrau_instrucao = async () => {
      const response = await api.get('/grau_instrucao/');
      setgrau_instrucao(response.data);
    };  
   
  const [nome_raca, setnome_raca] = useState([]);
  const fetchnome_raca = async () => {
      const response = await api.get('/raca/');
      setnome_raca(response.data);
    };    
  
  const [tipo_doencas, settipo_doencas] = useState([]);
  const fetchtipo_doencas = async () => {
      const response = await api.get('/tipo_doencas/');
      settipo_doencas(response.data);
    };
  
  const [tipo_cancer, settipo_cancer] = useState([]);
  
  
  const [parente_sangue, setparente_sangue] = useState([]);
  const fetchparente_sangue = async () => {
      const response = await api.get('/parente_sangue/');
      setparente_sangue(response.data);
    };

    const [origem, setorigem] = useState([]);
    const fetchorigem = async () => {
        const response = await api.get('/origem/');
        setorigem(response.data);
      };


  const trStyle = {
      backgroundColor: 'green',
      
      fontWeight: 'bold',
      borderTop:'4000px',
     
      // Adicione outros estilos conforme necessário
    };

  useEffect(() => {
    fetchGeneros();
    fetchPaises();
    fetchEstados();
    fetchsituacao_conjugal();
    fetchgrau_instrucao();
    fetchnome_raca();
    fetchtipo_doencas();
    fetchtipo_cancer();
    fetchparente_sangue();
    fetchorigem();

  }, []);

  const fetchtipo_cancer = async () => {
    const response = await api.get('/tipo_cancer/');
    settipo_cancer(response.data);
  };
    
  const [showStateField, setShowStateField] = useState(false);
  const [showStateFieldResidencia, setShowStateFieldResidencia] = useState(false);

  // Função para manipular a mudança de idade do diagnóstico de câncer
  const handleAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_paciente];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_paciente: newIdadeInicioCancers });
  };

  const handleFatherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_pai];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_pai: newIdadeInicioCancers });
  };

  const handleMotherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_mae];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_mae: newIdadeInicioCancers });
  };

  const handlePaternalGrandfatherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_avo_paterno];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_avo_paterno: newIdadeInicioCancers });
  };
  
  const handlePaternalGrandmotherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_avo_paterna];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_avo_paterna: newIdadeInicioCancers });
  };

  const handleMaternalGrandfatherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_avo_materno];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_avo_materno: newIdadeInicioCancers });
  };
  
  const handleMaternalGrandmotherAgeInputChange = (index, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_avo_materna];
    newIdadeInicioCancers[index] = value;
    setformData({ ...formData, idade_inicio_cancers_avo_materna: newIdadeInicioCancers });
  };

  const handleFilhosAgeInputChange = (index, idx, value) => {
    const newIdadeInicioCancers = [...formData.idade_inicio_cancers_filho];
    newIdadeInicioCancers[index] = newIdadeInicioCancers[index] || [];
    newIdadeInicioCancers[index][idx] = value;
    setformData({ ...formData, idade_inicio_cancers_filho: newIdadeInicioCancers });
  };
  


  const handleFormSubmit = async (event) => {
      event.preventDefault();
      await api.post('/submit-form/', formData);
      navigate("/resultado");
      window.scrollTo(0, 0);
    };


return (
  <div class='root'>

  <div className='container'>
    <nav className='navbar navbar-dark bg-success' class='navbar'>
      <div className='container-fluid'>
        <img src={logo} alt="Logo" className="navbar-brand" style={{width: '150px',  margin: 'auto'}} />
      </div>
    </nav>
    <form onSubmit={handleFormSubmit} class = "formulario">
        {/* Cada campo do formulário */}
      
        {renderOptionButtonGroupDiv(
          'O questionário será respondido:',
          consts.opcoesQuestionario,
          formData.quem_respondeu,
          (option) => setformData({ ...formData, quem_respondeu: option }),
        )}
        {renderOptionButtonGroupDiv(
          'Você já é paciente do AC Camargo Cancer Center?',
          consts.opcoesSimNao,
          formData.paciente,
          (option) => {
            if (option === 'Não') {
              // Se a opção selecionada for 'Não', remova o campo 'rgh' do estado
              const { rgh, ...newformData } = formData;
              setformData({ ...newformData, paciente: option });
            } else {
              // Se a opção selecionada for 'Sim', adicione o campo 'rgh' ao estado com um valor inicial vazio
              setformData({ ...formData, paciente: option, rgh: '' });
            }
          },
        )}
        {/* Adicione o campo rgh se a opção 'Sim' estiver selecionada */}
        {formData.paciente === 'Sim' && (
            <GenericInput
            type='text'
            label='RGH:'
            id='rgh'
            name='rgh'
            value={formData.rgh}
            setformData={setformData}
            formData={formData}
            />
          )}


        <GenericInput
          type="text"
          label="CPF"
          id="cpf"
          name="cpf"
          value={formData.cpf}
          setformData={setformData}
          formData={formData}
          maxLength={11}
        />

        <GenericInput
          type="text"
          label="Nome completo do paciente"
          id="nome_paciente"
          name="nome_paciente"
          value={formData.nome_paciente}
          setformData={setformData}
          formData={formData}
        />

        <GenericInput
          type="text"
          label="Nome completo da mãe"
          id="nome_mae"
          name="nome_mae"
          value={formData.nome_mae}
          setformData={setformData}
          formData={formData}
        />

        {renderOptionButtonGroupDiv(
          'Gênero:',
          generos.map(item => 
            (item.nome
          )),
          formData.genero,
          (option) => setformData({ ...formData, genero: option })
        )}

        <GenericInput
          type="date"
          label="Data de Nascimento"
          id="data_nascimento"
          name="data_nascimento"
          value={formData.data_nascimento}
          setformData={setformData}
          formData={formData}
        />

      <GenericSelect
          label="País de Residência"
          id="pais_residente"
          name="pais_residente"
          value={formData.pais_residente}
          onChange={(e) => {
            const selectedCountry = e.target.value;
            setformData({ ...formData, pais_residente: selectedCountry });
            setShowStateFieldResidencia(selectedCountry === 'Brasil');
          }}
          options={paises.map(item => 
            (item.nome
          ))}
      />
        
      {showStateFieldResidencia && (
        <GenericSelect
          label="Estado de Residência"
          id="estado_residente"
          name="estado_residente"
          value={formData.estado_residente}
          onChange={(e) => setformData({ ...formData, estado_residente: e.target.value })}
          options={estados.map(item => 
            (item.nome_estado
          ))}
        />
      )}
      <GenericInput
        type="text"
        label="Cidade de Residência"
        id="cidade_residente"
        name="cidade_residente"
        value={formData.cidade_residente}
        setformData={setformData}
        formData={formData}
      />

      <GenericInput
        type="text"
        label="CEP de Residência"
        id="cep_residente"
        name="cep_residente"
        value={formData.cep_residente}
        setformData={setformData}
        formData={formData}
        pattern="\d{5}-\d{3}" // Adiciona uma expressão regular para validar o formato do CEP
        title="Formato válido: 00000-000" // Fornece uma dica de formato para o usuário
      />
        
      {renderOptionButtonGroupDiv(
        'Qual a sua situação conjugal?',
        situacao_conjugal.map(item => 
          (item.nome_situacao
        )),
        formData.situacao_conjugal,
        (option) => setformData({ ...formData, situacao_conjugal: option })
      )}

      {renderOptionButtonGroupDiv(
        'Qual é o seu grau de instrução máximo?',
        grau_instrucao.map(item => 
          (item.nome_intrucao
        )),
        formData.grau_instrucao,
        (option) => setformData({ ...formData, grau_instrucao: option })
      )}

      {renderOptionButtonGroupDiv(
        'Na sua opinião qual é a sua cor/raça?',
        nome_raca.map(item => 
          (item.nome_raca
        )),
        formData.raca,
        (option) => setformData({ ...formData, raca: option })
      )}

      <GenericInput
        type="text"
        label="Qual a ocupação que você exerceu por mais tempo?"
        id="ocupacao"
        name="ocupacao"
        value={formData.ocupacao}
        setformData={setformData}
        formData={formData}
      />

      <GenericInput
        type="number"
        label="Por quanto tempo você exerceu essa ocupação?"
        id="tempo_ocupacao"
        name="tempo_ocupacao"
        value={formData.tempo_ocupacao}
        setformData={setformData}
        formData={formData}
      />

      <GenericInput
        type="text"
        label="Telefone para contato"
        id="telefone"
        name="telefone"
        value={formData.telefone}
        setformData={setformData}
        formData={formData}
      />

      <GenericInput
        type="email"
        label="Email"
        id="email"
        name="email"
        value={formData.email}
        setformData={setformData}
        formData={formData}
      />       

      <div class='sobre_voce'>
        <b>INFORMAÇÕES SOBRE VOCÊ</b>
      </div>   
      
      <GenericInput
        type="number"
        label="Qual a sua idade?"
        id="idade"
        name="idade"
        value={formData.idade}
        setformData={setformData}
        formData={formData}
      />
      
      <GenericSelect
        label="País de Origem"
        id="pais_origem"
        name="pais_origem"
        value={formData.pais_origem}
        onChange={(e) => {
          const selectedCountry = e.target.value;
          setformData({ ...formData, pais_origem: selectedCountry });
          setShowStateField(selectedCountry === 'Brasil');
        }}
        options={paises.map(item => 
          (item.nome
        ))}
      />
        {showStateField && (
          <GenericSelect
            label="Estado de Origem"
            id="estado_origem"
            name="estado_origem"
            value={formData.estado_origem}
            onChange={(e) => setformData({ ...formData, estado_origem: e.target.value })}
            options={estados.map(item => 
              (item.nome_estado
            ))}
          />
        )}

      <GenericInput
        type="text"
        label="Cidade de Origem"
        id="cidade_origem"
        name="cidade_origem"
        value={formData.cidade_origem}
        setformData={setformData}
        formData={formData}
      />
      
      {renderOptionButtonGroupDiv(
        'Você é adotado(a)?',
        consts.opcoesSimNao,
        formData.adotado==='true' ? 'Sim':'Não',
        (option) => setformData({ ...formData, adotado: option === 'Sim' ? 'true' : 'false' })
      )}
        
      {/* Você tem ou já teve algum desses diagnósticos? */}
      <div className="mb-3">
        <label>Você tem ou já teve algum desses diagnósticos?</label>
          {/* Renderizar diagnósticos */}
          {generateCheckboxes(
            tipo_doencas.map(item => 
              (item.nome_doenca
            )), formData.diagnosticos,
            (value, isChecked) => handleCheckboxChange(value, isChecked, "diagnosticos", formData, setformData))}
          {/* Campo de entrada para outro diagnóstico, visível apenas se "Outro" estiver marcado */}
          {formData.diagnosticos.includes('Outro') && (
            <input
              type="text"
              id="outro_diagnostico_input"
              className="form-control"
              value={formData.outroDiagnostico}
              onChange={(e) => setformData({ ...formData, outroDiagnostico: e.target.value })}
              placeholder="Especifique outro diagnóstico"
            />
          )}

      </div>

      {/* Você tem alguma lesão ou problema atualmente?*/}
      {renderOptionButtonGroupDiv(
      'Você tem alguma lesão ou problema atualmente?:',
      consts.opcoesLesaoAtual,
      formData.opcoes_tumor,
      (option) => setformData({ ...formData, opcoes_tumor: option })
      )}

      {(formData.opcoes_tumor === "Tenho tumor benigno/pólipo/nódulo benigno" || formData.opcoes_tumor === "Tenho tumor maligno/câncer") && (
        <div>
          <div className='mb-3 mt-3'>
            <label className='form-label'>Selecione o(s) tipo(s) de tumor(s):</label>
            {generateCheckboxes(
              tipo_cancer.map(item => 
                (item.nome
              )),
              formData.lesao_atual,
              (tumor, isChecked) => handleCheckboxChange(tumor, isChecked,'lesao_atual', formData, setformData)
            )}
          </div>

          <div className='mb-3 mt-3'>
            <label className='form-label'>Qual a sua idade no início do problema atual?</label>
            <GenericInput
              type='number'
              id='idade_inicio_lesao'
              name='idade_inicio_lesao'
              value={formData.idade_inicio_lesao}
              setformData={setformData}
              formData={formData}
            />
          </div>
        </div>
      )}

      {/* Pergunta: Fora a suspeita da lesão atual, você já teve câncer? */}
      {renderOptionButtonGroupDiv(
        'Fora a suspeita da lesão atual, você já teve câncer?',
        consts.opcoesSimNao,
        formData.teve_cancer ? 'Sim' : 'Não', // Convertendo booleano para string
        (option) => setformData({ ...formData, teve_cancer: option === 'Sim' })
      )}

      {/* Mostrar opções de diagnósticos de câncer se a resposta for 'Sim' */}
      {formData.teve_cancer && (
      <div>
        {/* Renderizar diagnósticos da família */}
        {generateCheckboxes(tipo_cancer.map(item => 
                (item.nome
              )), formData.cancers_que_teve_paciente, (value, isChecked) =>
          handleCheckboxChange(value, isChecked, "cancers_que_teve_paciente", formData, setformData)
        )}

        {/* Renderizar inputs para a idade do diagnóstico de câncer */}
        {formData.cancers_que_teve_paciente.map((cancer, index) => (
          <div key={index}>
            {(cancer !== 'Não sei onde começou' && cancer !== 'Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
              <input
                type="number"
                placeholder={`Idade do diagnóstico de ${cancer}`}
                value={formData.idade_inicio_cancers_paciente[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                onChange={(e) => handleAgeInputChange(index, e.target.value)}
              />
            )}
          </div>
        ))}
      </div>
      )}
    

      {/* Alguem da familia com algum diagnostico?*/}
      <div className="mb-3">
        <label>Alguém da sua família tem ou teve algum desses diagnósticos?</label>
        <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes( tipo_doencas.map(item => 
              (item.nome_doenca
            )), formData.familia_diagnosticos, (value, isChecked) =>
              handleCheckboxChange(value, isChecked, "familia_diagnosticos", formData, setformData)
            )}
          {/* Campo de entrada para outro diagnóstico da família, visível apenas se "Outro" estiver marcado */}
          {formData.familia_diagnosticos.includes('Outro') && (
              <input
                type="text"
                id="outro_familia_diagnostico_input"
                className="form-control"
                value={formData.familia_diagnostico_outro}
                onChange={(e) => setformData({ ...formData, familia_diagnostico_outro: e.target.value })}
                placeholder="Especifique outro diagnóstico da família"
              />
            )}
        </div>
      </div>
      {renderOptionButtonGroupDiv(
        'Você ou alguém da sua família já fez teste genético (de DNA) para risco de câncer?',
        consts.opcoesSimNaoNaoSei,
        formData.teste_genetico,
        (option) => setformData({ ...formData, teste_genetico: option })
      )}

      {renderOptionButtonGroupDiv(
        'Você acha que o câncer pode ser hereditário, ou seja, um problema genético da sua família?',
        consts.opcoesSimNaoNaoSei,
        formData.cancer_hereditario,
        (option) => setformData({ ...formData, cancer_hereditario: option })
      )}
      
      <div class='historico'>
        <b>AGORA VOCÊ VAI RESPONDER SOBRE O HISTÓRICO DE CÂNCER DE SUA FAMÍLIA</b>
      </div>

      <p>
      Você irá responder a um questionário sobre casos de câncer na sua família. Caso tenha qualquer dúvida, fale com os monitores que estão aplicando os questionários. É importante que você não deixe nenhuma pergunta em branco.
      </p> 

      {renderOptionButtonGroupDiv(
        'Seu pai teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_pai_cancer,
        (option) => setformData({ ...formData, opcao_pai_cancer: option })
        )}

        {(formData.opcao_pai_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.pai_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "pai_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.pai_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_pai[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handleFatherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
        </div>
        )}

      {renderOptionButtonGroupDiv(
        'Sua mae teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_mae_cancer,
        (option) => setformData({ ...formData, opcao_mae_cancer: option })
        )}

        {(formData.opcao_mae_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.mae_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "mae_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.mae_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_mae[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handleMotherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
          </div>
        )}

      {renderOptionButtonGroupDiv(
        'Seu pai e sua mãe são primos/parentes de sangue?',
        parente_sangue.map(item => 
          (item.nome
        )),
        formData.pais_parentes,
        (option) => setformData({ ...formData, pais_parentes: option })
        )}



      {renderOptionButtonGroupDiv(
        'Seu avô paterno teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_avo_paterno_cancer,
        (option) => setformData({ ...formData, opcao_avo_paterno_cancer: option })
        )}

        {(formData.opcao_avo_paterno_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.avo_paterno_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "avo_paterno_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.avo_paterno_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_avo_paterno[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handlePaternalGrandfatherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
          </div>
        )}

        <GenericSelect
          label="Qual a origem do seu avô paterno?"
          id="origem_avo_paterno"
          name="origem_avo_paterno"
          value={formData.origem_avo_paterno}
          onChange={(e) => setformData({ ...formData, origem_avo_paterno: e.target.value })}
          options={origem.map(item => 
            (item.nome_origem
          ))}
        />

     {renderOptionButtonGroupDiv(
        'Sua avó paterna teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_avo_paterna_cancer,
        (option) => setformData({ ...formData, opcao_avo_paterna_cancer: option })
        )}

        {(formData.opcao_avo_paterna_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.avo_paterna_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "avo_paterna_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.avo_paterna_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_avo_paterna[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handlePaternalGrandmotherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
          </div>
        )}

        <GenericSelect
          label="Qual a origem do sua avó paterna?"
          id="origem_avo_paterna"
          name="origem_avo_paterna"
          value={formData.origem_avo_paterna}
          onChange={(e) => setformData({ ...formData, origem_avo_paterna: e.target.value })}
          options={origem.map(item => 
            (item.nome_origem
          ))}
        />

      {renderOptionButtonGroupDiv(
        'Seu avô paterno e sua avó paterna são parentes de sangue?',
        parente_sangue.map(item => 
          (item.nome
        )),
        formData.avos_parentes_paterno,
        (option) => setformData({ ...formData, avos_parentes_paterno: option })
        )}


      {renderOptionButtonGroupDiv(
        'Seu avô materno teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_avo_materno_cancer,
        (option) => setformData({ ...formData, opcao_avo_materno_cancer: option })
        )}

        {(formData.opcao_avo_materno_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.avo_materno_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "avo_materno_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.avo_materno_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_avo_materno[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handleMaternalGrandfatherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
          </div>
        )}

        <GenericSelect
          label="Qual a origem do seu avô materno?"
          id="origem_avo_materno"
          name="origem_avo_materno"
          value={formData.origem_avo_materno}
          onChange={(e) => setformData({ ...formData, origem_avo_materno: e.target.value })}
          options={origem.map(item => 
            (item.nome_origem
          ))}
        />

      {renderOptionButtonGroupDiv(
        'Sua avó materna teve ou tem câncer?',
        consts.opcoesCancer,
        formData.opcao_avo_materna_cancer,
        (option) => setformData({ ...formData, opcao_avo_materna_cancer: option })
        )}

        {(formData.opcao_avo_materna_cancer === "Sim") && (
          <div>
          {/* Renderizar diagnósticos da família */}
          {generateCheckboxes(tipo_cancer.map(item => 
                  (item.nome
                )), formData.avo_materna_cancer, (value, isChecked) =>
            handleCheckboxChange(value, isChecked, "avo_materna_cancer", formData, setformData)
          )}

          {/* Renderizar inputs para a idade do diagnóstico de câncer */}
          {formData.avo_materna_cancer.map((cancer, index) => (
            <div key={index}>
              {(cancer !== 'Não sei onde começou' && cancer !=='Não sei se tenho') && ( // Não renderizar input para a opção "Não sei"
                <input
                  type="number"
                  placeholder={`Idade do diagnóstico de ${cancer}`}
                  value={formData.idade_inicio_cancers_avo_materna[index] || ''} // Usar a idade do estado ou uma string vazia se não estiver definida
                  onChange={(e) => handleMaternalGrandmotherAgeInputChange(index, e.target.value)}
                />
              )}
            </div>
          ))}
          </div>
        )}

        <GenericSelect
          label="Qual a origem do sua avó materna?"
          id="origem_avo_materna"
          name="origem_avo_materna"
          value={formData.origem_avo_materna}
          onChange={(e) => setformData({ ...formData, origem_avo_materna: e.target.value })}
          options={origem.map(item => 
            (item.nome_origem
          ))}
        />

      {renderOptionButtonGroupDiv(
        'Seu avô materno e sua avó materna são parentes de sangue?',
        parente_sangue.map(item => 
          (item.nome
        )),
        formData.avos_parentes_materno,
        (option) => setformData({ ...formData, avos_parentes_materno: option })
        )}



      {/* Pergunta: Algum filho seu tem ou teve câncer? */}
      {renderOptionButtonGroupDiv(
        'Algum filho seu tem ou teve câncer?',
        consts.opcoesSimNao,
        formData.algum_filho_tem_ou_teve_cancer ? 'Sim' : 'Não',
        (option) => setformData({ ...formData, algum_filho_tem_ou_teve_cancer: option === 'Sim' })
      )}

      {formData.algum_filho_tem_ou_teve_cancer && (
        <div>
          <GenericInput
            type="number"
            label="Quantos filhos já tiveram câncer?"
            id="quantidade_filho_cancer"
            name="quantidade_filho_cancer"
            value={formData.quantidade_filho_cancer}
            setformData={setformData}
            formData={formData}
          />

          {/* Renderizar perguntas sobre diagnósticos para cada filho com câncer */}
          {Array.from({ length: formData.quantidade_filho_cancer }, (_, index) => (
            <div key={index}>
              <p>Diagnóstico de câncer do Filho {index + 1}</p>
              {generateCheckboxes(
                tipo_cancer.map(item => item.nome),
                formData.tipo_cancer_filho[index] || [],
                (value, isChecked) =>
                  handleCheckboxChange2(value, isChecked, "tipo_cancer_filho", formData, setformData, index)
              )}

              {/* Verifica se formData.tipo_cancer_filho[index] é um array antes de renderizar os inputs */}
              {formData.tipo_cancer_filho[index]?.map((cancer, idx) => (
              <div key={idx}>
                {(cancer !== 'Não sei onde começou' && cancer !== 'Não sei se tenho') && (
                  <input
                    type="number"
                    placeholder={`Idade do diagnóstico de ${cancer}`}
                    value={formData.idade_inicio_cancers_filho[index]?.[idx] || ''}
                    onChange={(e) => handleFilhosAgeInputChange(index, idx, e.target.value)}
                  />
                )}
                </div>
                ))}
            </div>
          ))}
        </div>
      )}
      
      <button type='submit' className='btn btn-primary'>
        Submit
      </button>
    </form>
    
    <button className='btn btn-primary' onClick={() => navigate('/')} >
      Voltar para página inicial
    </button>
  
  </div>
</div>
);
}

export default App;