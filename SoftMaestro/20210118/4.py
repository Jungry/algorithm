#11047 동전 0

n,k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin = sorted(coin,reverse=True)
total = 0
for i in coin:
    if n == 0:
        break
    if k//i>0:
        total += k//i
        k = k%i
print(total)