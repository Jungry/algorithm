#Greedy - 큰 수의 법칙

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
#count = 0
#value = 0
#
data.sort()
#
large = data[-1]
second = data[-2]
#
#for i in range(m):
#    if count != k :
#        value += large
#        count += 1
#    elif count == k :
#        value += second
#        count = 0
#
#print(value)

#수열 이용
num =(large*k)+second
value = 0

value += (m//(k+1))*num
value += (m%(k+1))*large

print(value)