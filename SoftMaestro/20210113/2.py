#부품 찾기 (2 계수 정렬)

n = int(input())
data = [0] * 1000001

for i in input().split():
    data[int(i)] = 1

m = int(input())
bring = list(map(int,input().split()))

for i in bring:
    if data[i] == 1:
        print('YES',end=' ')
    else:
        print('NO',end=' ')