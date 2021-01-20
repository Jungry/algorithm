#2751 수 정렬하기 2

import sys 
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr,reverse = True)
for i in arr:
    print(i)