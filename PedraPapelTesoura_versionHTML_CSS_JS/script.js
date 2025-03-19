// Variáveis que armazenam o placar do jogador, computador e empates
let placarJogador = 0;
let placarComputador = 0;
let empates = 0;
let totalJogadas = 0;

// Função que processa a jogada do jogador e determina o resultado do jogo
function jogar(escolhaJogador) {
    document.getElementById("img-maoJogador").style.display = "inline";
    document.getElementById("img-maoComputador").style.display = "inline";

    const opcoes = ["pedra", "papel", "tesoura"];
    const escolhaComputador = opcoes[Math.floor(Math.random() * opcoes.length)];

    let resultado;

    totalJogadas++; // Incrementa o total de jogadas

    if (escolhaJogador === escolhaComputador) {
        resultado = "Empate!";
        empates++; // Incrementa o número de empates
    } else if (
        (escolhaJogador === "pedra" && escolhaComputador === "tesoura") || 
        (escolhaJogador === "papel" && escolhaComputador === "pedra") || 
        (escolhaJogador === "tesoura" && escolhaComputador === "papel")
    ) {
        resultado = "Você venceu!";
        placarJogador++;
    } else {
        resultado = "Computador venceu!";
        placarComputador++;
    }

    document.getElementById("img-jogador").style.display = "none";
    document.getElementById("img-computador").style.display = "none";

    document.querySelector(".player-choice").classList.add("shakePlayer");
    document.querySelector(".computer-choice").classList.add("shakeComputer");

    setTimeout(() => {
        document.getElementById("img-maoJogador").style.display = "none";
        document.getElementById("img-maoComputador").style.display = "none";

        document.getElementById("img-jogador").src = `${escolhaJogador}.png`;
        document.getElementById("img-computador").src = `${escolhaComputador}.png`;

        document.getElementById("img-jogador").style.display = "inline";
        document.getElementById("img-computador").style.display = "inline";

        document.getElementById("result-text").textContent = `Computador escolheu: ${escolhaComputador}. ${resultado}`;

        // Atualiza o placar na tela
        atualizarPlacar();
    }, 800);

    setTimeout(() => {
        document.querySelector(".computer-choice").classList.remove("shakeComputer");
        document.querySelector(".player-choice").classList.remove("shakePlayer");
    }, 1800);
}

function atualizarPlacar() {
    document.getElementById("player-score").textContent = placarJogador;
    document.getElementById("computer-score").textContent = placarComputador;
    document.getElementById("draw-score").textContent = empates;
    document.getElementById("total-games").textContent = totalJogadas;
}
