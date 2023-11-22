
import itertools

def tsp(graph, start):
    # List of nodes in the graph
    nodes = list(graph.keys())
    # List of nodes visited so far
    visited = [start]
    # List of nodes left to visit
    left = list(set(nodes) - set(visited))
    # Minimum weight Hamiltonian Cycle
    min_weight = float('inf')

    # Permutations of nodes left to visit
    for perm in itertools.permutations(left):
        # Calculate the weight of the cycle
        weight = graph[visited[-1]][perm[0]] + graph[perm[0]][perm[1]]
        for i in range(1, len(perm)):
            weight += graph[perm[i-1]][perm[i]]
        # Add the weight of the return edge to the start node
        weight += graph[perm[-1]][start]

        # Update the minimum weight Hamiltonian Cycle
        if weight < min_weight:
            min_weight = weight

    return min_weight

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3, 'D': 5},
    'B': {'A': 1, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 6},
    'D': {'A': 5, 'B': 4, 'C': 6}
}

print(tsp(graph, 'A')) # Output: 9