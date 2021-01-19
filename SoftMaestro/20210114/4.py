#랜선 자르기
import sys
k,n = map(int,sys.stdin.readline().rstrip().split())
array = []
for _ in range(k):
    array.append(int(input()))

start = 1
end = max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start + end) //2
    for x in array:
        if x >= mid:
            total += x//mid
    if total < n: #랜선이 부족한 경우
        end = mid - 1
    else: #충분한 경우
        result = mid
        start = mid + 1
print(result)

