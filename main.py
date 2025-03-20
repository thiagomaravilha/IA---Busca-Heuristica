import time
import itertools
from mapa import carregar_mapa, calcular_custo_terreno
from busca import a_star, calcular_rota
from interface import mostrar_mapa, mostrar_resultado
from mapa import GRID_SIZE

def main():
    mapa = carregar_mapa("mapa_42x42.txt")

    inicio = (6, 40)
    saida = (41, 40)

    # Identificar amigos no mapa
    amigos = {}
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if mapa[r][c] in "DELMW":
                amigos[mapa[r][c]] = (r, c)

    # Buscar a melhor rota
    melhor_custo = float('inf')
    melhor_rota = None
    melhor_ordem = None

    for ordem in itertools.permutations(amigos.items()):
        rota, custo = calcular_rota(mapa, inicio, ordem, saida)
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = rota
            melhor_ordem = ordem

    print("Melhor ordem para visitar os amigos:", [letra for letra, _ in melhor_ordem])

    # Exibir a movimentação no mapa
    custo_acumulado = 0
    for i, posicao in enumerate(melhor_rota):
        custo_passo = calcular_custo_terreno(mapa, posicao)
        custo_acumulado += custo_passo

        print(f"Passando por {posicao} - Terreno: {mapa[posicao[0]][posicao[1]]} - Custo acumulado: {custo_acumulado}")

        mostrar_mapa(mapa, posicao, amigos, saida, melhor_rota[:i + 1])
        time.sleep(0)

    # Mensagem final
    chegou_na_saida = melhor_rota[-1] == saida
    mostrar_resultado(custo_acumulado, chegou_na_saida)

if __name__ == "__main__":
    main()
