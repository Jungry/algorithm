#2750 수 정렬하기
import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = sorted(arr)
for i in arr:
    print(i)