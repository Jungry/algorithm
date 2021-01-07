#상하좌우

n = int(input())
data = list(map(str,input().split()))
x,y = 1,1 #출발좌표

#L R U D 좌표 설정하는거 제대로하자 !!!!!
dx = [0,0,-1,1]
dy = [-1,1,0,0]
type = ['L','R','U','D']

for i in data:
    for j in range(len(type)):
        if i ==  type[j]:
            nx = x+dx[j]
            ny = y+dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny  #x와 y의 값을 업데이트
    print(x,y)

print(x,y)