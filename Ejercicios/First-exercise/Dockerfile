# Usamos una imagen oficial de Python como base
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
COPY app.py .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la app
CMD ["python", "app.py"]