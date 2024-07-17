import React from 'react';
import './App.css';
import { FormControlLabel, Checkbox as MuiCheckbox} from '@mui/material';

// Função genérica para renderizar opções de um select
const renderSelectOptions = (options) => {
  return options.map((option, index) => (
    <option key={index} value={option}>
      {option}
    </option>
  ));
};

// Componente de seleção genérica
export const GenericSelect = ({ label, id, name, value, onChange, options, showField, fieldValue }) => (
  <div className='mb-3'>
    <label htmlFor={id} className='form-label'>
      {label}
    </label>
    <select
      className='form-select'
      id={id}
      name={name}
      onChange={onChange}
      value={value}
    >
      <option value=''>Selecione uma opção</option>
      {renderSelectOptions(options)}
    </select>
    {showField && fieldValue && (
      <div className='mb-3'>
        <label htmlFor={`${id}_detail`} className='form-label'>
          {`${label} detalhes`}
        </label>
        <input
          type='text'
          className='form-control'
          id={`${id}_detail`}
          name={`${name}_detail`}
          value={fieldValue}
          onChange={onChange}
        />
      </div>
    )}
  </div>
);

// Função genérica para manipular mudanças de entrada de dados
export const handleInputChange = (fieldName, value, setformData, formData) => {
  setformData(prevData => ({
    ...prevData,
    [fieldName]: value
  }));
};

// Componente genérico de entrada de dados
export const GenericInput = ({ type, label, id, name, value, setformData, formData, pattern, title }) => {
  const handleChange = (e) => {
    const newValue = e.target.value;
    handleInputChange(name, newValue, setformData, formData);
  };

  let inputElement;
  if (type === 'text' || type === 'email' || type === 'number' || type === 'date'|| type === 'checkbox') {
    inputElement = (
      <input
        type={type}
        className="form-control"
        id={id}
        name={name}
        value={value}
        onChange={handleChange}
        pattern={pattern}
        title={title}
      />
    );
  } else {
    console.error('Unsupported input type:', type);
    inputElement = <input type="text" className="form-control" />;
  }

  return (
    <div className="mb-3">
      <label htmlFor={id} className="form-label">
        {label}
      </label>
      {inputElement}
    </div>
  );
};

export const handleCheckboxChange = (item, isChecked, fieldName, formData, setformData) => {
  let newList;
  if (isChecked) {
    newList = [...formData[fieldName], item];
  } else {
    newList = formData[fieldName].filter(existingItem => existingItem !== item);
  }
  setformData(prevData => ({
    ...prevData,
    [fieldName]: newList
  }));
};

export const handleCheckboxChange2 = (item, isChecked, fieldName, formData, setformData, index) => {
  setformData(prevData => {
    const updatedFormData = { ...prevData };
    updatedFormData[fieldName] = updatedFormData[fieldName] || [];
    updatedFormData[fieldName][index] = updatedFormData[fieldName][index] || [];

    if (isChecked) {
      updatedFormData[fieldName][index].push(item);
    } else {
      updatedFormData[fieldName][index] = updatedFormData[fieldName][index].filter(existingItem => existingItem !== item);
    }

    return updatedFormData;
  });
};


// Componente funcional para renderizar uma checkbox
export function Checkbox({ label, isChecked, onChange }) {
  return (
    <div className="form-check">
      <FormControlLabel
        control={<MuiCheckbox checked={isChecked} onChange={onChange} />}
        label={label}
      />
    </div>
  );
}

// Função para renderizar várias checkboxes com base em uma lista de valores
export function generateCheckboxes(values, checkedValues, onChange) {
  return values.map((value, index) => (
    <Checkbox
      key={`checkbox_${index}`}
      label={value}
      isChecked={checkedValues.includes(value)}
      onChange={(e) => onChange(value, e.target.checked)}
    />
  ));
}