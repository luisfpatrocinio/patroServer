import asyncio
import websockets

# Guarda todos os clientes conectados
connectedClients = set();

# Servidor Echo
async def server(websocket, path):
    # Adciona um novo cliente a lista de clientes conectados
    print("Cliente conectado: " + str(websocket.remote_address))
    connectedClients.add(websocket)
    
    # Loop para receber mensagens do cliente:
    async for message in websocket:
        # Processar a mensagem recebida do cliente:
        print(f"Recebi a mensagem: {message}")
        
        # Mandando a mensagem para todos os clientes
        for conected in connectedClients:
            print("Mandando pacote para: " + str(conected.remote_address))
            await conected.send(message);
                        

# Iniciar o servidor:
start_server = websockets.serve(server, "", 8765)

# Executa o servidor indefinidamente
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()