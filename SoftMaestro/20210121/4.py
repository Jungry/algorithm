#1916 최소 비용 구하기
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    u,v,m = map(int,input().split())
    graph[u].append((v,m))

start,end = map(int,input().split())

dis = [INF] *(n+1)

def di(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        dist,now = heapq.heappop(q) #거리, 현재위치 꺼내기
        if dis[now] < dist: #꺼낸 값이 더 큰경우
            continue
        for i in graph[now]: #간선들 확인
            cost = dist + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] =cost
                heapq.heappush(q,(cost,i[0]))
di(start)

print(dis[end])
