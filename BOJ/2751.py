#시간을 줄이기 위해 sys 를 사용할 필요가 있음
import sys
n = int(input())

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array = sorted(array)
for i in array:
    print(i)

#print 대신 sys.stdout.write() 도 사용 가능