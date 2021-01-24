#간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input()) #시작노트
graph = [[] for i in range(n+1)] #노드들에 대한 정보 담기
visited = [False] * (n+1) #모두 방문 안함으로
distence = [INF] * (n+1)

for _ in range(m):  #간선 정보 입력받기
    a,b,c = map(int,input().split()) #a에서 b로 가는 비용이 c 라는 의미
    graph[a].append((b,c))

def get_small_node():
    min_val = INF
    index = 0
    for i in range(1,n+1):
        if distence[i] < min_val and not visited[i]:
            min_val = distence[i]
            index = i
    return index

def di(start): 
    #시작노드에 대해서 초기화
    distence[start] = 0
    visited[start] =  True
    for j in graph[start]:
        distence[j[0]] = j[1]
    for i in range(n-1):
        #현재 최단거지가 가장 짧은 노드 꺼내서 방문
        now = get_small_node()
        visited[now] = True
        for j in graph[now]: #현재 노드와 연결된 다른 노드 확인
            cost = distence[now] + j[1]
            if cost < distence[j[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distence[j[0]] = cost
di(start)

for i in range(1,n+1):
    if distence[i]== INF:
        print('NO')
    else:
        print(distence[i])