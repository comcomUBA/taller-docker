const http = require('http');
const { execSync } = require('child_process');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  const name = process.env.GREETING_NAME || 'Docker';
  const art = execSync(`/usr/games/cowsay ${name}`).toString();

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end(art);
});

server.listen(port, hostname, () => {
  console.log(`Servidor ejecutándose en http://${hostname}:${port}/`);
});
