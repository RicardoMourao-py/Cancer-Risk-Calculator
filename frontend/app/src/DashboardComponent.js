import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, Button } from '@mui/material';
import { PieChart } from '@mui/x-charts/PieChart';
import { Link } from 'react-router-dom'; // Importe o Link para navegação entre rotas
import logo from './logo.png';
import './App.css';
import api_predict from './api-predict';
import api from './api';
import { useFormData, initialFormData } from './formData';

const CombinedCharts = () => {
    const [prediction, setPrediction] = useState('');
    const [predictionProbaPositivo, setpredictionProbaPositivo] = useState('');
    const [predictionProbaNegativo, setpredictionProbaNegativo] = useState('');

    const [inputData, setInputData] = useState({});
    const { formData, setformData } = useFormData();

    const fetchPredict = async () => {
        try {
            // Faz a solicitação para /input-predict/ no backend
            const response_predict = await api.post('/input-predict/', formData);
            // Atualiza o estado inputData com os dados retornados
            setInputData(response_predict.data);

            // Faz a solicitação para /predict/ no backend usando os dados atualizados
            api_predict.post('/predict/', response_predict.data)
            .then(response => {
                // Atualize o estado com o resultado da previsão
                setPrediction(response.data.prediction);
                setpredictionProbaNegativo(response.data.predictionProba_negativo);
                setpredictionProbaPositivo(response.data.predictionProba_positivo);

            });
        } catch (error) {
            console.error('Erro:', error);
        }
    };

    useEffect(() => {
        // Chama a função fetchPredict quando o componente é montado
        fetchPredict();
    }, []);

    return (
        <div className='root'>
            <div className='container'>
                <nav className='navbar navbar-dark bg-success' class='navbar'>
                    <div className='container-fluid'>
                        <img src={logo} alt="Logo" className="navbar-brand" style={{ width: '150px', margin: 'auto' }} />
                    </div>
                </nav>
                <div className='dashboard'>
                    <Card variant="outlined" style={{ margin: '1rem'  }}>
                        <CardContent>
                            <Typography variant="h6" component="h2">
                                Resultado do Teste Genético
                            </Typography>
                            <Typography variant="body1" color="textSecondary">
                            <li>Esta ferramenta não pode calcular com precisão a indicação de ocorrência de algum tipo de mutação.</li>
                            <li>Esta ferramenta foi projetada para uso por profissionais de saúde. Se você não é um profissional de saúde, recomendamos imprimir esses resultados e discuti-los com seu médico.</li>
                            <li>
                                As respostas fornecidas foram utilizadas para estimar o a possibilidade de algum tipo de mutação, recomendando que o paciente faça um teste genético ou não.
                                Sendo assim, o modelo de previsão considera os seguintes fatores:
                                <ol>
                                    <li>Histórico de tumores do paciente;</li>
                                    <li>Histórico de câncer dos paciente;</li>
                                    <li>Histórico de câncer dos parentes do 1° e 2° grau.</li>
                                </ol>
                                Para mais informações de cada campo utilizado na predição, consulte a tabela no final da página.
                            </li>
                            </Typography>
                        </CardContent>
                    </Card>

                    <Card variant="outlined" style={{ margin: '1rem', backgroundColor: '#E8F5E9', boxShadow: '0 4px 8px 0 rgba(0,0,0,0.2)', transition: '0.3s', borderRadius: '15px' }}>
                        <CardContent>
                            <Typography variant="h6" component="h2" style={{ color: '#388E3C' }}>
                                Resultado do Teste Genético
                            </Typography>
                            <Typography variant="body1" color="textSecondary" style={{ marginTop: '1rem', color: '#689F38' }}>
                                {prediction}
            
                            </Typography>
                        </CardContent>
                    </Card>
                    <Card variant="outlined" style={{ margin: '1rem', backgroundColor: '#E8F5E9', boxShadow: '0 4px 8px 0 rgba(0,0,0,0.2)', transition: '0.3s', borderRadius: '15px' }}>
                        <CardContent>
                            <Typography variant="h6" component="h2" style={{ color: '#388E3C' }}>
                                Probabilidades de ocorrência de mutação baseadas no teste genético
                            </Typography>
                            <div style={{ margin: '1rem' }}>
                                <PieChart
                                    series={[
                                        {
                                            data: [
                                                { id: 0, value: predictionProbaPositivo, label: 'Positivo' },
                                                { id: 1, value: predictionProbaNegativo, label: 'Negativo' },
                                                
                                            ],
                                        },
                                    ]}
                                    width={400}
                                    height={200}
                                />
                            </div>
                        </CardContent>
                    </Card>
                    
                    <div className='table-container'>
                        <table>
                            <thead>
                                <tr>
                                    <th>Perguntas</th>
                                    <th>Respostas</th>
                                    {/* Adicione mais colunas conforme necessário */}
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Você tem alguma lesão ou problema atualmente?</td>
                                    <td>{formData.opcoes_tumor}</td>
                                </tr>
                                <tr>
                                    <td>Quais lesões você tem atualmente?</td>
                                    <td>{formData.lesao_atual[0]}</td>
                                </tr>
                                <tr>
                                    <td>Qual a sua idade no início do problema atual?</td>
                                    <td>{formData.idade_inicio_lesao}</td>
                                </tr>
                                <tr>
                                    <td>Fora a suspeita da lesão atual, você já teve câncer?</td>
                                    <td>{formData.teve_cancer ? 'Sim' : 'Não'}</td>
                                </tr>
                                <tr>
                                    <td>Quais canceres você já teve?</td>
                                    <td>{formData.cancers_que_teve_paciente[0]}</td>
                                </tr>
                                <tr>
                                    <td>Seu pai teve ou tem câncer?</td>
                                    <td>{formData.opcao_pai_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve seu pai?</td>
                                    <td>{formData.pai_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Sua mãe teve ou tem câncer?</td>
                                    <td>{formData.opcao_mae_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve sua mãe?</td>
                                    <td>{formData.mae_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Seu avô paterno teve ou tem câncer?</td>
                                    <td>{formData.opcao_avo_paterno_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve seu avô paterno?</td>
                                    <td>{formData.avo_paterno_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Sua avó paterna teve ou tem câncer?</td>
                                    <td>{formData.opcao_avo_paterna_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve sua avó paterna?</td>
                                    <td>{formData.avo_paterna_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Seu avô materno teve ou tem câncer?</td>
                                    <td>{formData.opcao_avo_materno_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve seu avô materno?</td>
                                    <td>{formData.avo_materno_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Sua avó materna teve ou tem câncer?</td>
                                    <td>{formData.opcao_avo_materna_cancer}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve sua avó materna?</td>
                                    <td>{formData.avo_materna_cancer[0]}</td>
                                </tr>
                                <tr>
                                    <td>Quais cânceres teve seus filhos?</td>
                                    <td>{formData.tipo_cancer_filho[0]}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    {/* Botões para voltar à rota principal ou à rota do formulário */}
                    <div>
                        <Link to="/" style={{ marginRight: '1rem' }}>
                            <Button variant="contained">Voltar para a Página Principal</Button>
                        </Link>
                        <Link to="/formulario">
                            <Button variant="contained">Ir para o Formulário</Button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CombinedCharts;
