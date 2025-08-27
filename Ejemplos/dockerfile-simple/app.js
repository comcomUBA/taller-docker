const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  
  // Mensaje que varía según el entorno
  const environment = process.env.NODE_ENV || 'production';
  let message = '¡Hola desde Node.js en Docker!';
  
  if (environment === 'development') {
    message = '¡Hola desde Node.js en Docker! - MODO DESARROLLO';
    console.log('Solicitud recibida en modo desarrollo');
  }
  
  res.end(message + '\n');
});

server.listen(port, hostname, () => {
  console.log(`Servidor ejecutándose en http://${hostname}:${port}/`);
  console.log(`Entorno: ${process.env.NODE_ENV || 'production'}`);
});