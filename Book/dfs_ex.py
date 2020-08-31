#dfs 예제
#dfs 메서드 정의

def dfs(graph , v , visited): #v 현재 노드 visited 방문한 노드
    #현재 노드를 방문 처리
    visited[v] = True
    print(v,end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
#하나씩 타고 들어가서 방문 안한애 있으면 재귀
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited =[False]*9

dfs(graph,1,visited)