#피보나치 수열
def fibo(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(35))

d = [0] * 100

def fibo2(n):
    if n ==1 or n ==2:
        return 1
    
    if d[n]!=0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo2(35))

d = [0] * 100
d[1] =1
d[2] = 1
n=35

for i in range(3,n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])