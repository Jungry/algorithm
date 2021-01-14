#숫자 카드 

n = int(input())
arr = set(map(int,input().split()))

m=int(input())
check = list(map(int,input().split()))

for i in check:
    if i in arr:
        print(1,end=' ')
    else:
        print(0,end=' ')