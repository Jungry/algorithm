#나무 자르기
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

start = 1
end = max(arr)
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x >= mid:
            total += x-mid
    if total < m: #부족한 경우 (mid 를 줄여야함)
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)