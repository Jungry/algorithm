#떡볶이 떡 만들기

#떡의 개수와 요청한 떡의 길이
n,m = list(map(int,input().split()))

#각 떡의 개별 높이 정보를 입력받기
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += x - mid 
    #떡 양이 부족하면 더 많이 잘라야함 (왼쪽 탐색)
    if total < m:
        end = mid -1
    #떡 양이 충분하면 덜 잘라야함 (오른쪽 탐색)
    else:
        result = mid #최대한 덜 잘랐을때가 정답이니까 result 에 저장
        start = mid + 1
print(result)
