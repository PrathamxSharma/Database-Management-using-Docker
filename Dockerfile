# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY analyze_orders.py analyze_orders.py
COPY orders.csv orders.csv

CMD ["python", "analyze_orders.py"]