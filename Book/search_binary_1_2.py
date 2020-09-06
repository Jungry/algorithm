#부품찾기 (반복문)

def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int,input().split()))
m = int(input())
array_target = list(map(int.input().split()))

for i in array_target:
    result = binary_search(array,i,0,n-1)
    if result == None:
        print('no',end = ' ')
    else:
        print('yes',end =' ')