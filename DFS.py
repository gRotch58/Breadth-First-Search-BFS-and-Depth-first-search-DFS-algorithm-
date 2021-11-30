
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['2', '3']),
         '2': set(['1', '4', '5']),
         '3': set(['1']),
         '4': set(['2']),
         '5': set(['3', '4'])}

print(" Depth First  Search: ")

dfs(graph, '1')