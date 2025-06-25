import sys
import time

class BranchAndBoundAprimorado:
    def __init__(self, grafo):
        self.g = grafo
        self.n = len(grafo)
        self.caminho = [-1] * self.n
        self.min_custo = sys.maxsize
        self.melhor = []
        self.visitados = 0

    def e_valido(self, v, pos):
        if self.g[self.caminho[pos-1]][v] == 0 or v in self.caminho[:pos]:
            return False
        return True

    def limite_inferior(self, custo, pos):
        estimativa = 0
        visitado = [False] * self.n
        for i in range(pos):
            visitado[self.caminho[i]] = True

        for i in range(self.n):
            if not visitado[i]:
                menores = sorted([self.g[i][j] for j in range(self.n) if self.g[i][j] > 0])
                if len(menores) >= 2:
                    estimativa += (menores[0] + menores[1]) / 2
                elif menores:
                    estimativa += menores[0]

        if pos < self.n:
            ult = self.caminho[pos - 1]
            retorno = [self.g[ult][j] for j in range(self.n) if not visitado[j] and self.g[ult][j] > 0]
            if retorno:
                estimativa += min(retorno)

        return custo + estimativa

    def resolver(self, custo, pos):
        self.visitados += 1

        if pos == self.n:
            fim = self.g[self.caminho[pos - 1]][self.caminho[0]]
            if fim > 0:
                total = custo + fim
                if total < self.min_custo:
                    self.min_custo = total
                    self.melhor = list(self.caminho)
            return

        if self.limite_inferior(custo, pos) >= self.min_custo:
            return

        for v in range(self.n):
            if self.e_valido(v, pos):
                self.caminho[pos] = v
                self.resolver(custo + self.g[self.caminho[pos-1]][v], pos + 1)
                self.caminho[pos] = -1

    def vizinho_mais_proximo(self):
        visitado = [False] * self.n
        caminho = [0] * self.n
        atual = 0
        visitado[0] = True
        custo = 0

        for i in range(1, self.n):
            prox, menor = -1, sys.maxsize
            for j in range(self.n):
                if not visitado[j] and 0 < self.g[atual][j] < menor:
                    menor = self.g[atual][j]
                    prox = j
            if prox == -1:
                return [], sys.maxsize
            caminho[i] = prox
            custo += menor
            visitado[prox] = True
            atual = prox

        if self.g[caminho[-1]][caminho[0]] > 0:
            custo += self.g[caminho[-1]][caminho[0]]
            return caminho, custo
        return [], sys.maxsize

    def encontrar(self):
        self.caminho[0] = 0
        self.visitados = 0
        self.min_custo = sys.maxsize
        self.melhor = []

        ini = time.time()
        guloso, custo_guloso = self.vizinho_mais_proximo()
        if custo_guloso != sys.maxsize:
            self.min_custo = custo_guloso
            self.melhor = list(guloso)

        self.resolver(0, 1)
        fim = time.time()

        if self.min_custo == sys.maxsize:
            return None, None, (fim - ini) * 1000, self.visitados
        return self.melhor + [self.melhor[0]], self.min_custo, (fim - ini) * 1000, self.visitados

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
    solver = BranchAndBoundAprimorado(grafo)
    caminho, custo, tempo, nos = solver.encontrar()
    print("--- Vizinho Mais Próximo + Branch and Bound ---")
    print(f"Caminho: {caminho}")
    print(f"Custo: {custo}")
    print(f"Tempo: {tempo:.3f} ms")
    print(f"Nós visitados: {nos}")
