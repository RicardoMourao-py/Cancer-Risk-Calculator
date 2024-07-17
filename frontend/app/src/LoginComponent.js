import React from 'react';
import { Card, CardContent, Typography, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './App.css';

import logo from './logo.png';

const App = () => {
    window.scrollTo(0, 0);

    const navigate = useNavigate();
    
    return (
        <div className='root'>
            <div className='container'>
                <nav className='navbar navbar-dark bg-success' class='navbar'>
                    <div className='container-fluid'>
                        <img src={logo} alt="Logo" className="navbar-brand" style={{ width: '150px', margin: 'auto' }} />
                    </div>
                </nav>
                <div className='dashboard'>
                    <Card variant="outlined" style={{ margin: '4rem' }}>
                        <CardContent>
                            <Typography variant="h6" component="h2">
                                Bem-vindo ao Sistema de Teste Genético
                            </Typography>
                            <Typography variant="body1" color="textSecondary">
                                Este sistema permite fazer previsões com base em dados genéticos.
                            </Typography>
                        </CardContent>
                    </Card>
                    <Typography variant="body1" color="textSecondary" style={{ marginTop: '2rem' }}>
                        Você responderá as perguntas do formulário de forma verdadeira?
                    </Typography>
                    <div>
                        <Button variant="contained" onClick={() => navigate('/formulario')} style={{ margin: '1rem' }}>Sim</Button>
                        <Button variant="contained" style={{ margin: '1rem' }}>Não</Button>
                    </div>
                    
                </div>
            </div>
        </div>
    );
}

export default App;
