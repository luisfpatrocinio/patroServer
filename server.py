from http.server import BaseHTTPRequestHandler, HTTPServer

# Classe para lidar com requisições HTTP:
class RequestHandler(BaseHTTPRequestHandler):
    # Método para lidar com requisições GET:
    def do_GET(self):
        # Configurar cabeçalho da resposta:
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Enviar o corpo da resposta:
        self.wfile.write(b'Olar.')


# Iniciar o servidor:
def run(port=8000):
    # Cria uma instância do servidor HTTP:
    print('Iniciando servidor...')
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Servidor iniciado na porta {port}.')

    try:
        # Mantém o servidor em execução:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Encerra o servidor caso o usuário pressione Ctrl+C:
        httpd.server_close()
        print('Servidor encerrado.')


# Inicia o servidor na porta 8000:
if __name__ == '__main__':
    run()