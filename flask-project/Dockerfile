FROM python:3.13-slim

WORKDIR /app

COPY app.py .
COPY requirement.txt .

RUN pip install -r requirement.txt

CMD ["python", "app.py"]