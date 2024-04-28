FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask mysql-connector-python

CMD ["python", "main.py"]
