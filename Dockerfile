FROM python:3.9-slim

WORKDIR /app

# Copiamos el código
COPY api.py /app
COPY alerts.py /app
COPY requirements.txt /app

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# La app corre en el puerto 5001 (como en api.py)
EXPOSE 5001

# Comando para ejecutar la API
CMD ["python", "api.py"]
