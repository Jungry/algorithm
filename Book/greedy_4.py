#1이 될때까지
n,k = map(int,input().split())
count =0

while n != 1:
    if n%k != 0:
        count += 1
        n -= 1
    else:
        count += 1
        n = n//k
print(count)