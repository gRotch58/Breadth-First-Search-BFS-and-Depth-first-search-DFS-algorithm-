


import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:


        vertex = queue.popleft()
        print(str(vertex) + " ", end="")



        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {1: [2, 3], 2: [3], 3: [4], 4: [2, 3]}
    print(" Breadth First Traversal: ")
    bfs(graph, 1)