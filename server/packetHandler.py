# A classe pacote serve para mandar as informações para o usuário, tem um comando e valores

# Arquivo que só serve pra manipular "objetos" (dicionários, não consegui javanizar o python) de Pacote
def newPacket(command, values):
    return {
        "command" : command,
        "values" : values
    }
