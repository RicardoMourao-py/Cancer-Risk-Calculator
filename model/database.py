# database.py
from pathlib import Path
import pandas as pd
from dotenv import dotenv_values
import mysql.connector

# Este módulo contém funções para conectar a um banco de dados MySQL e exportar dados para um arquivo CSV.

def main():
    """Função principal para conectar ao banco de dados, executar uma consulta SQL e exportar os resultados para um arquivo CSV."""
    # Conectar ao banco de dados MySQL
    try:
        env = dotenv_values(".env")
        connection = mysql.connector.connect(
            host=env.get('DB_HOST'),
            user=env.get('DB_USER'),
            password=env.get('DB_PASSWORD'),
            database=env.get('DB_DATABASE_NAME')
        )
        print("Conexão bem-sucedida.")

        # Ler a consulta do arquivo SQL
        sql_file_path = Path('sql') / '002_onpremise_table.sql'
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            query = file.read()

        # Executar a consulta e ler os resultados em um DataFrame
        dataframe = pd.read_sql(query, connection)
        print(dataframe)

        # Exportar o DataFrame para um arquivo CSV
        csv_file_path = Path('app/data') / 'dados_exportados.csv'
        dataframe.to_csv(csv_file_path, index=False)
        print("DataFrame exportado para CSV com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
    except FileNotFoundError as error:
        print(f"Erro ao abrir o arquivo: {error}")
    finally:
        # Fechar a conexão ao banco de dados
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexão fechada.")

if __name__ == "__main__":
    main()
