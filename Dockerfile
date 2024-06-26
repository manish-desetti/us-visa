
FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]