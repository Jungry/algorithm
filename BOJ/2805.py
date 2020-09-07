#나무 자르기 (pypy 로 해결시 해결됨)
import sys

n,m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i-mid
    if total <m: #나무가 적은 경우 (end 조정)
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)
    