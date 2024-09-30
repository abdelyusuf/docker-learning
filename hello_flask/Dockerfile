#stage 1:build
FROM python:3.8-slim as BUILD

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

    COPY . .

    RUN pip install flask mysqlclient

    #stage 2: Production stahe

    FROM python:3.8-slim

    WORKDIR /app

    COPY --from=BUILD /app /app/

    EXPOSE 5002

    CMD [ "python", "app.py" ]
     
