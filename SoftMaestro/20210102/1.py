#그리디 숫자카드게임
#나의 풀이

n,m = map(int,input().split())
result = 0
for i in range(n): #n번 반복
    num = list(map(int,input().split())) #숫자 입력
    minn = min(num)
    if result <= minn:
        result = minn
print(result)

#책의 풀이

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    minn = min(data)
    result = max(result,minn)
print(result)