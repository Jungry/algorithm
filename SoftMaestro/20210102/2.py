#1이 될때까지
#나의 풀이

n,k = map(int,input().split())
result = 0
while True:
    if n%k == 0:
        result +=1
        n //=k
        if n == 1:
            break
    else:
        result +=1
        n -=1
        if n == 1:
            break
print(result)

#책의 풀이
n,k = map(int,input().split())
result = 0

while n>=k:
    while n%k !=0:
        n-=1
        result += 1
    n//=k
    result += 1

while n>1:
    n -=1
    result += 1
print(result)