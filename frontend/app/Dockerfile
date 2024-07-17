# Use a imagem base do Node.js
FROM node:14

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do package.json para o contêiner
COPY package.json package-lock.json /app/

# Instala as dependências
RUN npm install

# Copia o código da aplicação para o contêiner
COPY . .

# Comando para iniciar o servidor de desenvolvimento do React
CMD ["npm", "start"]