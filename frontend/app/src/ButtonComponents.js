import React from 'react';
import {Table, TableBody, TableCell, TableHead, TableRow,ButtonGroup, Button } from '@mui/material';
import * as consts from './consts';


export const OptionButtonGroup = ({ options, selectedOption, onSelect }) => {
  const handleClick = (option) => {
    // Se o botão clicado já estiver selecionado, desmarque-o
    const newSelectedOption = selectedOption === option ? null : option;
    onSelect(newSelectedOption);
  };

  return (
    <ButtonGroup aria-label="Opções" class='option-button'>
      {options.map((option, index) => (
        <Button
          key={index}
          variant={selectedOption === option ? 'contained' : 'outlined'}
          onClick={() => handleClick(option)}
        >
          {option}
        </Button>
      ))}
    </ButtonGroup>
  );
};

// Função para renderizar uma div com um grupo de botões de opção
export const renderOptionButtonGroupDiv = (labelText, options, selectedOption, onSelect) => (
  <div className='mb-3' class='botoes'>
    <label className='form-label'>{labelText}</label>
    <OptionButtonGroup
      options={options}
      selectedOption={selectedOption}
      onSelect={onSelect}
    />
  </div>
  
);

export const renderTable = (headerText, includeCancerButtons, includeParentescoButtons,style) => {
  return (
    <Table style={style}>
      <TableHead>
        <TableRow>
          <TableCell className="header toolbar" colSpan={3}>
            <div data-mlm-field="data_respostas" data-mlm-type="header">
              {headerText}
            </div>
          </TableCell>
          {includeCancerButtons && (
            <TableCell className="header toolbar" colSpan={3}>
              <div>
                Teve ou tiveram câncer
              </div>
              {consts.opcoesCancer.map((opcao, index) => (
                <Button key={index} variant="contained" color="primary">
                  {opcao}
                </Button>
              ))}
            </TableCell>
          )}
          {includeParentescoButtons && (
            <TableCell className="header toolbar" colSpan={3}>
              <div>
                Tem parentesco
              </div>
              {consts.parentesco_sangue.map((opcao, index) => (
                <Button key={index} variant="contained" color="primary">
                  {opcao}
                </Button>
              ))}
            </TableCell>
          )}
        </TableRow>
      </TableHead>
      <TableBody>
        {/* Aqui você pode adicionar o conteúdo da tabela usando TableRow e TableCell */}
      </TableBody>
    </Table>
  );
};