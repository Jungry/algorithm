#부품 찾기(재귀함수)

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2 #중간값
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    
n = int(input())
array = list(map(int,input().split()))
array = sorted(array)
m = int(input())
array_target = list(map(int,input().split()))

for i in range(m):
    result = binary_search(array,array_target[i],0,n-1)
    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')