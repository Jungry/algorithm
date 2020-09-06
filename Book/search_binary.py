#이진 탐색 소스코드 구현 (재귀함수)

def binary_search(array,target,start,end):
    if start>end :
        return None
    mid = (start+end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array,target,start,mid-1)
    #큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)
    
n,target = list(map(int,input().split()))
#전체 원소 입력
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 없습니다")
else:
    print(result+1)