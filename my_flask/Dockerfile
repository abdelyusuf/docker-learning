FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask redis

EXPOSE 5002

CMD [ "python", "app.py" ]