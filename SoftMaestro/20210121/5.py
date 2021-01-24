#1238 파티
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split()) #n:학생수 m:도로수 x:파티장소
graph = [[] for i in range(n+1)]
dis1 = [INF] * (n+1) #갈때
dis2 = [INF] * (n+1) #올때

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

#집에 돌아올때
def die(start,dis):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return dis

die(x,dis2)
#print(dis2)
result = [0]
for i in range(1,len(graph)):
    start = i
    dis1 = [INF] * (n+1)
    die(start,dis1)
    #print(dis1[x])
    result.append(dis2[i]+dis1[x])
print(max(result))


