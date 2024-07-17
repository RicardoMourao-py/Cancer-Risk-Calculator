# Use uma imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de dependências e instala no contêiner
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . /app

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]