#1753 최단 경로
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split()) #v=정점의 개수 e=간선의 개수
start = int(input())

#노드들의 정보 담기
graph = [[] for i in range(n+1)]
#최단거리 저장할곳
dis = [INF] * (n+1)

for _ in range(e): #간선 입력받기
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) #5 -> 1 가중치 1 

def di(start):
    q = [] #우선순위큐
    heapq.heappush(q,(0,start)) #q에 start 를 거리 0으로 넣는다
    dis[start] = 0 #시작의 거리는 0 으로
    while q: #큐에 값이 들어있는동안 반복
        dist,now = heapq.heappop(q) #거리와 현재 위치를 꺼낸다
        if dis[now] < dist: #지금 들어온거보다 더 짧은게 저장되어있는 경우 (이미 처리한 적이 있는거임)
            continue
        for i in graph[now]: #현재 노드의 간선들을 확인해보자 !
            cost = dist + i[1]
            if dis[i[0]] > cost: #거쳐서 이동하면 더 짧아지는 경우
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
di(start)

for i in range(1,n+1):
    if dis[i] == INF:
        print('INF')
    else:
        print(dis[i])
