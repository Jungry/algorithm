#상하좌우 이동 문제
n = int(input())
move = list(map(str,input().split()))

x,y = 1,1
move_x = [0,0,-1,1]
move_y = [-1,1,0,0]
move_type =['L','R','U','D']

for i in move:
    for j in range(len(move_type)):
        if i == move_type[j]:
            test_x = x+move_x[j]
            test_y = y+move_y[j]

    if test_x < 1 or test_x > n or test_y < 1 or test_y > n:
        continue
    else:
        x,y = test_x,test_y
    
print(x,y)