# Arquivo que só serve pra manipular "objetos" (dicionários, não consegui javanizar o python) de mensagem
def newMessage(userId, owner, timestamp, content):
    return {
        "userId": userId,
        "owner" : owner,
        "timestamp" : timestamp,
        "content" : content
    }