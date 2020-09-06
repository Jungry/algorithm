#1920 수 찾기

#use set
n = int(input())
array = set(map(int,input().split()))
m = int(input())
array_target = list(map(int,input().split()))

for i in array_target:
    if i in array:
        print('1')
    else:
        print('0')

#use binary search
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target :
            end = mid -1
        else:
            start = mid +1
    return None

n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
array_target = list(map(int,input().split()))

for x in array_target:
    result = binary_search(array,x,0,n-1)
    if result == None:
        print('0')
    else:
        print('1')