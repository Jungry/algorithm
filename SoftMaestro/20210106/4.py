from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = True
    #큐가 빌때까지 반봅
    while queue:
        v = queue.popleft()
        print(v,end =' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],  #0은 없으니까 비워두자
    [2,3,8],  #1번 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)