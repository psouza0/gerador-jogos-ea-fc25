FROM python:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y build-essential python3-dev
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]