from http.server import BaseHTTPRequestHandler, HTTPServer

# Classe para lidar com requisições HTTP:
class RequestHandler(BaseHTTPRequestHandler):
    # Método para lidar com requisições GET:
    def do_GET(self):
        # Configurar cabeçalho da resposta:
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        try:
            # Abre e lê o conteúdo do arquivo
            with open('content.txt') as file:
                content = file.read()

            # Envia o conteúdo do arquivo como resposta
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            # Se o arquivo não for encontrado, retorna uma mensagem de erro
            error_message = "O arquivo não foi encontrado."
            self.wfile.write(error_message.encode('utf-8'))


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