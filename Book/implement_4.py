#게임 개발
n,m = map(int,input().split())

#이동 한적있는지 확인하기
d=[[0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y] = 1

#지도 입력받기
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

#북 동 남 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 0
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #move
    if d[nx][ny] == 0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: #can't move
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0 : #종결
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    
print(count)