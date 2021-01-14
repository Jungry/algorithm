#수 찾기
import sys

n = int(sys.stdin.readline().rstrip())
arr = set(map(int,sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
check = list(map(int,sys.stdin.readline().rstrip().split()))

for i in check:
    if i in arr:
        print(1)
    else:
        print(0)