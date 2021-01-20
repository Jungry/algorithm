#2752 세수 정렬
import sys
arr = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
for i in arr:
    print(i,end=' ')