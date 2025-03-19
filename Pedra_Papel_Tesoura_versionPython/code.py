import tkinter as tk
from PIL import Image, ImageTk  # Adicionado para manipulação de imagens
import random

# Função para carregar e redimensionar imagens
def carregar_imagem(nome_arquivo, largura=150, altura=150):
    """Carrega e redimensiona a imagem para um tamanho adequado"""
    imagem_original = Image.open(nome_arquivo)  # Abre a imagem
    imagem_redimensionada = imagem_original.resize((largura, altura), Image.LANCZOS) # Redimensiona
    return ImageTk.PhotoImage(imagem_redimensionada)  # Converte para uso no Tkinter

# Função principal do jogo
def jogar(escolha_jogador):
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)

    # Define o resultado da partida
    if escolha_jogador == escolha_computador:
        resultado = "Empate!"
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
         (escolha_jogador == "papel" and escolha_computador == "pedra") or \
         (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        resultado = "Você venceu!"
    else:
        resultado = "Computador venceu!"

    # Atualiza o texto do resultado
    label_resultado.config(text=f"Computador escolheu: {escolha_computador}\n{resultado}")

    # Alterado para carregar e redimensionar imagens corretamente
    imagem_jogador = carregar_imagem(f"{escolha_jogador}.png", 150, 150)  
    imagem_computador = carregar_imagem(f"{escolha_computador}.png", 150, 150)

    # Atualiza as imagens exibidas na tela
    label_imagem_jogador.config(image=imagem_jogador)
    label_imagem_jogador.image = imagem_jogador  # Mantém referência

    label_imagem_computador.config(image=imagem_computador)
    label_imagem_computador.image = imagem_computador  # Mantém referência

# Criando a interface gráfica
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")

label_instrucao = tk.Label(root, text="Escolha: Pedra, Papel ou Tesoura", font=("Arial", 14))
label_instrucao.pack()

# Criando rótulos para exibir as imagens
frame_jogo = tk.Frame(root)
frame_jogo.pack()

label_imagem_jogador = tk.Label(frame_jogo)
label_imagem_jogador.pack(side=tk.LEFT, padx=20)

label_imagem_computador = tk.Label(frame_jogo)
label_imagem_computador.pack(side=tk.RIGHT, padx=20)

# Botões para escolher Pedra, Papel ou Tesoura
frame_botoes = tk.Frame(root)
frame_botoes.pack()

botao_pedra = tk.Button(frame_botoes, text="Pedra", command=lambda: jogar("pedra"), width=10)
botao_pedra.grid(row=0, column=0, padx=5)

botao_papel = tk.Button(frame_botoes, text="Papel", command=lambda: jogar("papel"), width=10)
botao_papel.grid(row=0, column=1, padx=5)

botao_tesoura = tk.Button(frame_botoes, text="Tesoura", command=lambda: jogar("tesoura"), width=10)
botao_tesoura.grid(row=0, column=2, padx=5)

# Rótulo para exibir o resultado
label_resultado = tk.Label(root, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

root.mainloop()
 # type: ignore