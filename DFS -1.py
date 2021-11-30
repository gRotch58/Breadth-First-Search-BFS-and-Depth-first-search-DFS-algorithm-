
graph = {
  'E' : ['C','G'],
  'C' : ['B', 'D'],
  'G' : ['H'],
  'B' : [],
  'D' : ['H'],
  'H' : []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print(" Depth First Search")
dfs(visited, graph, 'E')