#11407 동전 0 
n,k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.reverse()
#print(coin)
result = 0

for x in coin:
    if k//x > 0: #나눌 수 있는 경우 (result 에 더해주고 k값 수정)
        result += (k//x)
        k %= x
    if k == 0:
        break
print(result)