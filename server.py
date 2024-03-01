import asyncio
import websockets

# Servidor Echo
async def server(websocket, path):
    # Loop para receber mensagens do cliente:
    async for message in websocket:
        # Processar a mensagem recebida do cliente:
        print(f"Recebi a mensagem: {message}")

        # Reenviar a mensagem para o jogo.
        await websocket.send(message)

# Iniciar o servidor:
start_server = websockets.serve(server, "", 8765)

# Executa o servidor indefinidamente
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()