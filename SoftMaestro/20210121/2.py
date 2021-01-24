#개선된 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
#노드들의 정보를 담기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distence = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def di(start):
    q = []
    heapq.heappush(q,(0,start)) #큐에 삽입
    distence[start] = 0
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있으면 무시
        if distence[now] < dist:
            continue
        #현재 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재를 거쳐서 다른 노드로 이동하는게 더 짧은 경우
            if distence[i[0]] > cost:
                distence[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
di(start)

for i in range(1,n+1):
    if distence[i] == INF:
        print('NO')
    else:
        print(distence[i])