SELECT 
    p.id_paciente,
    p.genero_id,
    p.situacao_conjugal_id,
    p.grau_instrucao_id,
    p.adotado,
    p.cancer,
    CASE 
        WHEN p.parentesco_pais_id = 1 OR p.parentesco_avosm_id = 1 OR p.parentesco_avosp_id = 1 THEN 1
        ELSE 0
    END AS Consanguinidade,
    pc.id_cancer AS paciente_cancer_id,
    pc.idade AS paciente_cancer_idade,
    pa.id_parente,
    pa.id_parentesco,
    pcn.id_cancer AS parente_cancer_id,
    pcn.idade AS parente_cancer_idade,
    op.id_origem,
    rg.id_gene,
    rg.id_tipo_proc,
    rg.resultado
FROM 
    Paciente p
LEFT JOIN 
    PacienteCancer pc ON p.id_paciente = pc.id_paciente
LEFT JOIN 
    Parente pa ON p.id_paciente = pa.id_paciente
LEFT JOIN 
    ParenteCancer pcn ON pa.id_parente = pcn.id_parente
LEFT JOIN 
    OrigemParente op ON pa.id_parente = op.id_parente
LEFT JOIN 
    ResultadoGenetico rg ON p.id_paciente = rg.id_paciente