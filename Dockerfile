# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos necessários para o contêiner
COPY . /app

# Instalar as dependências do Python
RUN pip install -r requirements.txt

# Expor a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python", "app.py"]
