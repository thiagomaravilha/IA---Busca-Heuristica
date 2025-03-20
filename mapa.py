# Tamanho do mapa
GRID_SIZE = 42

# Custos de movimentação nos terrenos
custos_terreno = {
    '.': 1,  # Piso seco
    '~': 3,  # Piso escorregadio
    'X': 6,  # Fiação exposta
    '=': 4   # Porta
}

# Representação de parede
IMPASSAVEL = '#'

def carregar_mapa(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return [list(linha.strip()) for linha in f.readlines()]

def calcular_custo_terreno(mapa, posicao):
    r, c = posicao
    return custos_terreno.get(mapa[r][c], 1)
