
// Criar Conexão WebSocket
// const websocketUrl = "ws://localhost:8765";
const websocketUrl = 'wss://patroserver.onrender.com/:8765';
const socket = new WebSocket(websocketUrl);

const userID = uuidv4();

var failed = false;
var pointsCounter = 0;

// Alterar texto do loadingMsg
setInterval(function() {
    if (pointsCounter == 3) {
        pointsCounter = 0;
        // Tentar reconectar
        // socket = new WebSocket(websocketUrl);
    } else {
        pointsCounter++;
    }

    if (!failed) {
        var loadingMsg = document.getElementById("loadingMsg");
        loadingMsg.textContent = "CONECTANDO-SE AO SERVIDOR" + ".".repeat(pointsCounter);
    }
}, 500);

// Conexão Aberta
socket.addEventListener('open', function (event) {
    console.log('Conexão Aberta');
    var mainPage = document.getElementById("mainPage");
    mainPage.style.display = "block";
    var loadingMsg = document.getElementById("loadingMsg");
    loadingMsg.style.display = "none";
});

// Conexão Fechada
socket.addEventListener('close', function (event) {
    console.log('Conexão Fechada');

    var loadingMsg = document.getElementById("loadingMsg");
    loadingMsg.style.display = "block";
    loadingMsg.innerHTML = "ERRO AO CONECTAR AO SERVIDOR<br><br>POR FAVOR ATUALIZE A PÁGINA";

    var mainPage = document.getElementById("mainPage");
    mainPage.style.display = "none";

    var failedMsg = document.getElementById("returnMsg");
    failedMsg.style.display = "block";  

    failed = true;
});

// Receber Mensagem
socket.addEventListener('message', function (event) {
    console.log('Mensagem Recebida: ' + event.data);
    // Criar objeto com informações recebidas:
    var _playerInfo = JSON.parse(event.data);

    var _type = _playerInfo.command;

    if (_type == "PLAYER_LOGIN") {
        // Nome no pacote:
        var _name = _playerInfo.values.name;

        // Nome no formulário:
        var _playerName = document.getElementById("playerName").value;

        if (_name === _playerName) {
            console.log("Você está conectado.")
            // Informar que o jogador está conectado
            var playerConnected = document.getElementById("playerConnected");
            playerConnected.textContent = "JOGADOR CONECTADO";
            playerConnected.style.display = "block";
        }
    }

    if (_type == "PLAYER_MESSAGE") {
        var _name = _playerInfo.values.name;
        var _message = _playerInfo.values.message;
        createMessageBlock(_name, _message);
    }


    if (_type == "MESSAGE_HISTORY"){
        var _messages = _playerInfo.values;
        for(_message of _messages){
            createMessageBlock(_message.owner, _message.content)
        }
    }
    
});

// Criar um bloco de mensagem no html
function createMessageBlock(name, message) {
    console.log("Criando bloco de mensagem")
    const chatSection = document.getElementById("chatSection");
    const newMessage = document.createElement("div");
    newMessage.className = "chatMessage";
    newMessage.innerHTML = `${name} : ${message}`;
    chatSection.appendChild(newMessage);
}

// Enviar Mensagem
function sendMessage() {

    var campo = document.getElementById("playerName");
    var aviso = document.getElementById("aviso");

    campo.addEventListener("input", function() {
        campo.classList.remove("error");
        aviso.style.display = "none";
    });
    
    if (campo.value === "") {
        campo.classList.add("error");
        aviso.textContent = "Informe seu nome de jogador.";
        aviso.style.display = "block"; // Exibe o aviso
        return false; // Impede o envio do formulário
    }

    var _playerInfo = {};

    // Obter texto inserido pelo usuário:
    _playerInfo.command = "PLAYER_MESSAGE";
    _playerInfo.values = {};
    _playerInfo.values.userId = String(userID);
    _playerInfo.values.name = String(document.getElementById("playerName").value).toUpperCase();
    _playerInfo.values.message = String(document.getElementById("playerMessage").value).toUpperCase();

    var jsonData = JSON.stringify(_playerInfo); 

    console.log(`Dados enviados: ${jsonData}`);
    
    var playerName = _playerInfo.values.name;

    if (playerName == "ADMIN_LABIRAS") {
        // Acessar Painel de Administrador
        window.location.href = "admin_panel.html?name=" + encodeURIComponent(playerName);
    } else {
        // Enviar mensagem:
        socket.send(jsonData);
        
        // Limpar campo:
        document.getElementById("playerMessage").value = "";

        // DESATIVADO: Mudar de página para player_panel.html:
        // window.location.href = "player_panel.html?name=" + encodeURIComponent(playerName);
    }
    
}

function deleteMessages() {
    const messageBlocksOnHtml = document.getElementsByClassName("chatMessage")
}

function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
    }