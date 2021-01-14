import sys
n,m = map(int,input().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))

#시작과 끝점 지정
start = 0
end = max(array)

result = 0

while start<= end:
    total = 0
    mid = (start+end)//2
    for x in array:
        if x>mid: #떡 길이가 더 긴경우
            total += x-mid
    if total < m: #떡이 부족한 경우(끝 감소)
        end = mid-1
    else: #떡이 충분한 경우 (중간값을 조정)
        result = mid
        start = mid + 1
print(result)
