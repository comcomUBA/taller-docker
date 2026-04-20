# Usar la imagen oficial de Node.js
FROM node:18-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y cowsay

# Copiar archivos de definición de dependencias
COPY package.json ./

# Instalar dependencias
RUN npm install

# Copiar el código de la aplicación
COPY app.js .

# Exponer el puerto que usa la aplicación
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
