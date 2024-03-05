import json
import os
from typing import List
# Eu pego o caminho do diretório em que eu estou em relação a todo o sistema
dirname = os.path.dirname(__file__);


def dumpsJSON(dict):
    return json.dump(dict);


def parseJSON(strObj):
    return json.loads(strObj);


# Encarregado de pegar um arquivo de uma localização e entregar ele pronto
def loadJSON(fileLocation):
    # Eu junto a localização global à localização local do messages.json
   with open((os.path.join(dirname, fileLocation)), "r") as file:
       content = json.load(file);
       return content;


def saveJSON(fileLocation, newObjects):
    
    # Se o tipo não for um dicionário
    if type(newObjects) == "str":
        newObjects = json.loads(newObjects)
    
    # Já começa com um valor dicionario (a biblioteca json dá erro caso nulo)
    jsonContent = loadJSON(fileLocation);
    
    # Adcionando novos objetos
    jsonContent.append(newObjects);
    
    # Json para String codificada em UTF-8
    jsonStrContent = json.dumps(jsonContent, indent=2, ensure_ascii= False).encode("UTF-8");
    
    file = open(os.path.join(dirname, fileLocation), "w+");
    file.write(jsonStrContent.decode());
    file.close();
    
    
if __name__ == "__main__":
    jasao = loadJSON("messages.json");