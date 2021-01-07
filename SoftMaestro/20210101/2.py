#큰수의 법칙
#내가 푼 방법

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

while True:
    for _ in range(k):
        if m == 0 :
            break
        result += first
        m -= 1
        if m == 0:
            break
    if m ==0:
        break
    result += second
    m -= 1

print(result)

#또 다른 풀이 (내꺼)
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

first = data[-1]
second  = data[-2]

value = (first*k)+second
result = 0

result += int(m/(k+1))*value
result +=  int(m%(k+1))*first
print(result)

#또 다른 풀이 (책)

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count * first
result += (m-count)*second

print(result)


