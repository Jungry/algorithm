#11728 배열 합치기
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = []
for _ in range(2):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

arr = sorted(sum(arr,[]))
for i in arr:
    print(i,end=' ')