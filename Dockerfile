FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache tzdata

# Holt die Requirements aus deinem Projektordner
COPY monitor-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiert den gesamten Code aus monitor-app in das /app Verzeichnis des Containers
COPY monitor-app/ .

CMD ["python", "app.py"]
