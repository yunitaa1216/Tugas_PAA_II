# Yunita anggeraini
# F55121070
# Kelas B
import sys
def tsp(graph, visited, current_vertex, n, count, cost, path):
    if count == n and graph[current_vertex][0]:
        path.append(0)
        return cost + graph[current_vertex][0], path

    for i in range(n):
        if not visited[i] and graph[current_vertex][i]:
            visited[i] = True
            path.append(i)
            new_cost, new_path = tsp(graph, visited, i, n, count + 1, cost + graph[current_vertex][i], path)

            if new_cost < cost:
                cost = new_cost
                path = new_path

            visited[i] = False
            path.pop()

    return cost, path


def traveling_salesman(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    path = [0]
    cost, path = tsp(graph, visited, 0, n, 1, 0, path)

    return cost, path


# Contoh penggunaan
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = traveling_salesman(graph)
print("Total Cost:", cost)
print("Path:", path)