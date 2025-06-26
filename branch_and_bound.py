import sys
import time

class BranchAndBound:
    def __init__(self, grafo):
        self.grafo = grafo
        self.n = len(grafo)
        self.caminho = [-1] * self.n
        self.melhor_caminho = []
        self.custo_min = sys.maxsize
        self.visitados = 0

    def e_valido(self, v, pos):
        if self.grafo[self.caminho[pos - 1]][v] == 0:
            return False
        return v not in self.caminho[:pos]

    def limite_inferior(self, custo_atual, pos):
        estimativa = 0
        visitado = [False] * self.n
        for i in range(pos):
            visitado[self.caminho[i]] = True

        for i in range(self.n):
            if not visitado[i]:
                menores = sorted([self.grafo[i][j] for j in range(self.n) if self.grafo[i][j] > 0])
                if len(menores) >= 2:
                    estimativa += (menores[0] + menores[1]) / 2
                elif len(menores) == 1:
                    estimativa += menores[0]

        return custo_atual + estimativa

    def resolver(self, custo_atual, pos):
        self.visitados += 1

        if pos == self.n:
            ultimo = self.caminho[pos - 1]
            if self.grafo[ultimo][self.caminho[0]] > 0:
                total = custo_atual + self.grafo[ultimo][self.caminho[0]]
                if total < self.custo_min:
                    self.custo_min = total
                    self.melhor_caminho = list(self.caminho)
            return

        if self.limite_inferior(custo_atual, pos) >= self.custo_min:
            return

        for v in range(self.n):
            if self.e_valido(v, pos):
                self.caminho[pos] = v
                self.resolver(custo_atual + self.grafo[self.caminho[pos - 1]][v], pos + 1)
                self.caminho[pos] = -1

    def encontrar_ciclo(self):
        self.caminho[0] = 0
        inicio = time.time()
        self.resolver(0, 1)
        fim = time.time()

        if self.custo_min == sys.maxsize:
            return None, None, (fim - inicio) * 1000, self.visitados
        else:
            ciclo = self.melhor_caminho + [self.melhor_caminho[0]]
            return ciclo, self.custo_min, (fim - inicio) * 1000, self.visitados

if __name__ == '__main__':
    grafo = [
    [0, 10, 8, 9, 7],
    [10, 0, 10, 5, 6],
    [8, 10, 0, 8, 9],
    [9, 5, 8, 0, 6],
    [7, 6, 9, 6, 0]
    ]

    solver = BranchAndBound(grafo)
    caminho, custo, tempo, nos = solver.encontrar_ciclo()

    print("--- Branch and Bound Padrão ---")
    print(f"Caminho: {caminho}")
    print(f"Custo: {custo}")
    print(f"Tempo: {tempo:.3f} ms")
    print(f"Nós visitados: {nos}")