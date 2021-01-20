#1654 랜선 자르기
import sys
k,n = map(int,sys.stdin.readline().rstrip().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = sorted(arr)

start = 1
end = max(arr)

result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x >= mid:
            total += x//mid
    if total < n: #모자란 경우 mid 값을 줄여야함
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
