import React, { useState } from 'react';
import { Route, Routes} from "react-router-dom"
import FormComponent from './FormComponent';
import DashboardComponent from './DashboardComponent';
import Login from './LoginComponent';


const App = () => {

  return (
    <div className='app'>
      <Routes>
        <Route path="/" element={<Login />}/>
        <Route path="/formulario" element={<FormComponent />}/>
        <Route path="/resultado" element={<DashboardComponent />}/>
      </Routes>
    
    </div>
  );
};

export default App;
