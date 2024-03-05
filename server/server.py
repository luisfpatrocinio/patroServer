import utils # biblioteca de utilidades própria
import asyncio # assincronia em python
import websockets 
import messageHandler # arquivo criado para métodos para lidar com mensagens

from datetime import datetime

# Guarda todos os clientes conectados
connectedClients = set();


# Servidor Echo
async def server(websocket, path):
    
    # Adciona um novo cliente a lista de clientes conectados
    print("Cliente conectado: " + str(websocket.remote_address))
    connectedClients.add(websocket)
    
    try:
    # Loop para receber mensagens do cliente:
        async for messageStr in websocket:
            # Processar a mensagem recebida do cliente:
            print(f"Recebi a mensagem: {messageStr}")
            
            # Transformando a mensagem em um dicionário python
            message = utils.parseJSON(messageStr);
            
            # Se o pacote recebido for uma mensagem, ele é salvo dentro do json de mensagens
            if message["command"] == "PLAYER_MESSAGE":
                
                # pegando o corpo da mensagem
                values = message["values"]
                
                # Convertendo o que ta vindo no formato de uma mensagem
                messageIntance = messageHandler.newMessage(owner=values["name"], 
                                                           timestamp=datetime.now().timestamp(), 
                                                           content=values["message"])
                
                # Salvando a mensagem criada dentro do arquivo json de mensagens
                utils.saveJSON("messages.json", messageIntance);
                
                #TODO: Mandar todas as mensagens para todos os players, pelo menos no primeiro acesso
                #TODO: Apagar as mensagens a cada X tempo
                
            # Mandando a mensagem para todos os clientes
            for conected in connectedClients:
                print("Mandando pacote para: " + str(conected.remote_address))
                await conected.send(messageStr);
    finally:
        connectedClients.remove(websocket);
        
def main():
    # Iniciar o servidor:
    start_server = websockets.serve(server, "", 8765)

    # Executa o servidor indefinidamente
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main();