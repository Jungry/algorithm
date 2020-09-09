#피보나치 수열 

def fibo(x):
    if x == 1 or x == 2 :
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

print(fibo(5))

#피보나치 수열 (메모이제이션)

d = [0] * 100

#피보나치 함수를 재귀함수로 구현 (탑 다운 다이나믹 프로그래밍)
def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+ fibo(x-2)
    return d[x]

print(fibo2(5))

#피보나치 함수 (반복적 , 보텀업)
b = [0] * 100

b[1] = 1
b[2] = 1
n = 99

for i in range(3,n+1):
    b[i]= b[i-1]+b[i-2]
print(b[99])