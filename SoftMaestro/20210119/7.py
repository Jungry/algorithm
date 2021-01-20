#2512 예산
import sys
n = int(sys.stdin.readline().rstrip())
money = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())

start = 1
end = max(money)

result = 0

while start <= end:
    total = 0 
    mid = (start+end) // 2
    for x in money:
        if x > mid:
            total += mid
        else:
            total += x
    if total > m: #금액이 초과가 된 경우 (금액을 줄여아함 end 조정)
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)