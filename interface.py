import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib
matplotlib.use('TkAgg')
from mapa import GRID_SIZE


def mostrar_mapa(mapa, posicao_agente=None, amigos=None, saida=None, caminho=None):
    plt.clf()

    terrenos = {'.': 0, '~': 1, 'X': 2, '=': 3, '#': 4}
    img = np.array([[terrenos.get(mapa[r][c], 0) for c in range(GRID_SIZE)] for r in range(GRID_SIZE)])

    cmap = ListedColormap(['lightgray', 'blue', 'red', 'saddlebrown', 'dimgray'])
    plt.imshow(img, cmap=cmap, origin='upper')

    if caminho:
        xs, ys = zip(*[(c + 0.5, r + 0.5) for r, c in caminho])
        plt.plot(xs, ys, color='black', linewidth=2)

    if amigos:
        for letra, (r, c) in amigos.items():
            plt.text(c + 0.5, r + 0.5, letra, color='yellow', fontsize=12, ha='center', va='center', fontweight='bold')

    if saida:
        r, c = saida
        plt.scatter(c + 0.5, r + 0.5, marker='o', s=100, facecolors='none', edgecolors='yellow')

    if posicao_agente:
        r, c = posicao_agente
        plt.scatter(c + 0.5, r + 0.5, marker='o', s=100, color='green')

    plt.pause(0.1)

def fechar_tela(event):
    plt.close('all')

def mostrar_resultado(custo_total, sucesso):
    plt.figure(figsize=(6, 5))
    plt.axis('off')

    mensagem = "Sucesso! Eleven encontrou a saída!" if sucesso else "Falha! Eleven não conseguiu escapar."
    cor = 'green' if sucesso else 'red'

    plt.text(0.5, 0.8, "FIM", fontsize=40, ha='center', va='center', color='darkblue', fontweight='bold')
    plt.text(0.5, 0.6, mensagem, fontsize=14, ha='center', va='center', color=cor, fontweight='bold')
    plt.text(0.5, 0.5, f"Custo Total: {custo_total}", fontsize=14, ha='center', va='center', color='black')

    # Botao Fechar
    botao_x, botao_y, botao_largura, botao_altura = 0.25, 0.15, 0.5, 0.15
    plt.gca().add_patch(plt.Rectangle((botao_x, botao_y), botao_largura, botao_altura, edgecolor='black', facecolor='lightgray'))
    plt.text(0.5, 0.225, "Fechar", fontsize=14, ha='center', va='center', color='black', fontweight='bold')

    # Capturar clique
    plt.gcf().canvas.mpl_connect('button_press_event', fechar_tela)

    plt.show()
