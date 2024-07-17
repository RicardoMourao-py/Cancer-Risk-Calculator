USE pfe_dev;

SELECT 
	id_paciente as Paciente, 
    adotado as Adotado,
    if (parentesco_pais_id = 1, 0, 1) as "Consaguinidade",
    GROUP_CONCAT(id_cancer) as "Tipo de Câncer"
FROM 
	Paciente
    LEFT OUTER JOIN PacienteCancer USING (id_paciente)
GROUP BY
	id_paciente;
