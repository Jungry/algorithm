#1476 날짜 계산

E,M,S = map(int,input().split())
start = 1

while True:
    if ((start-E)%15 == 0 and (start-M)%28 ==0 and (start-S)%19==0):
        break
    else:
        start += 1
print(start)