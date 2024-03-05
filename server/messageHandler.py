# Arquivo que só serve pra manipular "objetos" (dicionários, não consegui javanizar o python) de mensagem
def newMessage(owner, timestamp, content):
    return {
        "owner" : owner,
        "timestamp" : timestamp,
        "content" : content
    }