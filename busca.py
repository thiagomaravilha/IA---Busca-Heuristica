import heapq
from mapa import GRID_SIZE, custos_terreno, IMPASSAVEL


def heuristica(a, b):
    """heurística Manhattan entre dois pontos."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(mapa, inicio, destino):
    fila = []
    heapq.heappush(fila, (heuristica(inicio, destino), 0, inicio, [inicio]))
    visitados = set()

    while fila:
        _, custo, atual, caminho = heapq.heappop(fila)

        if atual == destino:
            return caminho, custo

        if atual in visitados:
            continue
        visitados.add(atual)

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = atual[0] + dr, atual[1] + dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and mapa[nr][nc] != IMPASSAVEL:
                novo_custo = custo + custos_terreno.get(mapa[nr][nc], 1)
                heapq.heappush(fila,
                               (novo_custo + heuristica((nr, nc), destino), novo_custo, (nr, nc), caminho + [(nr, nc)]))

    return None, float('inf')


def calcular_rota(mapa, inicio, amigos, saida):
    custo_total = 0
    caminho_completo = []
    atual = inicio

    for _, posicao in amigos:
        caminho, custo = a_star(mapa, atual, posicao)
        if caminho is None:
            return None, float('inf')
        custo_total += custo
        caminho_completo.extend(caminho if not caminho_completo else caminho[1:])
        atual = posicao

    caminho, custo = a_star(mapa, atual, saida)
    if caminho is None:
        return None, float('inf')
    custo_total += custo
    caminho_completo.extend(caminho[1:])

    return caminho_completo, custo_total
