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
        [0, 29, 20, 21, 16, 31, 100],
        [29, 0, 15, 29, 28, 2, 100],
        [20, 15, 0, 4, 10, 15, 100],
        [21, 29, 4, 0, 12, 28, 100],
        [16, 28, 10, 12, 0, 19, 100],
        [31, 2, 15, 28, 19, 0, 100],
        [100, 100, 100, 100, 100, 100, 0]  
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
