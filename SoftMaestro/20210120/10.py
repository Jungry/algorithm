#10867 중복 빼고 정렬하기

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr = sorted(set(arr))
for i in arr:
    print(i,end=' ')