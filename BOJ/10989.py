#count sort 를 이용해서 풀어보아용
#숫자의 범위가 10000 까지라는 조건이 있기 때문에 count 를 10001 까지 해주자
import sys

n = int(input())

count = [0]*10001

for _ in range(n):
    x = int(sys.stdin.readline())
    count[x] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)