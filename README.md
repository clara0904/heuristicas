# Heurísticas para o Problema do Ciclo Hamiltoniano

Este projeto implementa e compara três heurísticas para resolver o **Problema do Ciclo Hamiltoniano**. As heurísticas analisadas são:

- **Vizinho Mais Próximo**
- **Branch and Bound**
- **Versão Híbrida (Branch and Bound com Solução Inicial Gulosa)**

---

## Objetivo

O objetivo do projeto é analisar o desempenho de diferentes abordagens para encontrar o ciclo hamiltoniano de menor custo em um grafo. A comparação é baseada em:

- Custo total da solução encontrada  
- Tempo de execução  
- Número de nós visitados durante a busca

---

## Heurísticas Implementadas

### 1. Vizinho Mais Próximo

Uma heurística gulosa que, a partir de um vértice inicial, sempre escolhe o vizinho mais próximo ainda não visitado.

- Rápido  
- Pode não encontrar a melhor solução

### 2. Branch and Bound

Algoritmo exato que explora todas as possibilidades de caminho, mas poda ramos com custo superior ao mínimo atual.

- Encontra a melhor solução  
- Pode ser lento em instâncias grandes

### 3. Versão Híbrida

Combina os dois anteriores: utiliza o Vizinho Mais Próximo para gerar uma solução inicial que serve como limite superior no Branch and Bound, melhorando o desempenho da poda.

- Melhora a eficiência do Branch and Bound  
- Mantém a qualidade da solução
