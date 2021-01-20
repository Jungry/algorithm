#11004 K번째 수
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr =sorted(list(map(int,sys.stdin.readline().rstrip().split())))

print(arr[m-1])