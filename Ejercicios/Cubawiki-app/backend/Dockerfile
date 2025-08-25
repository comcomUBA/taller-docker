# Imagen base oficial de Python
FROM python:3.11-slim

# Configuración básica
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero (aprovechar cache de Docker)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

# Exponer el puerto del backend
EXPOSE 5000

# Comando de inicio
CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0", "--port=5000"]