import sys
import time

def vizinho_mais_proximo(grafo):
    n = len(grafo)
    visitado = [False] * n
    caminho = [0] * n
    atual = 0
    visitado[0] = True
    custo = 0
    nos_visitados = 1  

    for i in range(1, n):
        prox, menor = -1, sys.maxsize
        for j in range(n):
            nos_visitados += 1  
            if not visitado[j] and 0 < grafo[atual][j] < menor:
                menor = grafo[atual][j]
                prox = j
        if prox == -1:
            return [], sys.maxsize, nos_visitados
        caminho[i] = prox
        custo += menor
        visitado[prox] = True
        atual = prox

    if grafo[caminho[-1]][caminho[0]] > 0:
        custo += grafo[caminho[-1]][caminho[0]]
        return caminho + [caminho[0]], custo, nos_visitados
    return [], sys.maxsize, nos_visitados

if __name__ == '__main__':
    grafo = [
    [0, 10, 8, 9, 7],
    [10, 0, 10, 5, 6],
    [8, 10, 0, 8, 9],
    [9, 5, 8, 0, 6],
    [7, 6, 9, 6, 0]
    ]

    inicio = time.time()
    caminho, custo, nos_visitados = vizinho_mais_proximo(grafo)
    fim = time.time()
    tempo_ms = (fim - inicio) * 1000

    print("--- Heurística do Vizinho Mais Próximo ---")
    print(f"Caminho: {caminho}")
    print(f"Custo: {custo}")
    print(f"Tempo de execução: {tempo_ms:.3f} ms")
    print(f"Nós visitados: {nos_visitados}")
