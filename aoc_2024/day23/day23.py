from typing import List, Dict, Set
from collections import defaultdict, deque

def get_graph(filename) -> Dict[str, List[str]]:
    graph = defaultdict(list)
    
    fin = open(filename)
    pairs = [pair.split("-") for pair in fin.read().splitlines()]
    for p in pairs:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])
    return graph

def get_cliques(start: str, graph: Dict[str, List[str]], limit: int = 3) -> Set[tuple]:
    to_visit = deque()
    cliques = set()

    to_visit.append((start, [start]))  # Start with the start node in the path

    while to_visit:
        node, path = to_visit.popleft()
        
        if len(path) == limit:
            # Check if all nodes in path are connected to each other
            is_clique = True
            for i in range(len(path)):
                for j in range(i + 1, len(path)):
                    if path[j] not in graph[path[i]]:
                        is_clique = False
                        break
                if not is_clique:
                    break
                    
            if is_clique:
              cliques.add(tuple(sorted(path))) # Use sorted tuple as path order does not matter to form a clique
            continue

        for neighbor in graph[node]:
            if neighbor not in path:
                to_visit.append((neighbor, path + [neighbor]))  # Extend the path with the neighbor
            
    return cliques

graph = get_graph("input.txt")
res = set()

for node in graph.keys():
    if node.startswith("t"):
        cliques = get_cliques(node, graph)
        for clique in cliques:
            res.add(clique)

print(len(res))


def BronKerbosch(P, R=None, X=None):
    if R is None:
      R = []
    if X is None:
      X = []
    if not P and not X:
        yield R
        return
    
    for v in list(P):  # Iterate over a copy of P
        yield from BronKerbosch(
                [u for u in P if u in graph[v]],
                R + [v],
                [u for u in X if u in graph[v]])
        P.remove(v)
        X.append(v)


best = sorted(BronKerbosch(list(graph.keys())), key = len)[-1]
print(','.join(sorted(best)))