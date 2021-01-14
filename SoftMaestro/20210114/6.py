#숫자 카드

n = int(input())
arr = sorted(list(map(int,input().split())))

m=int(input())
check = list(map(int,input().split()))

def bin(array,target,start,end):
    if start > end :
        return None 
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin(array,target,start,mid-1)
    else:
        return bin(array,target,mid+1,end)
    
for i in check:
    result = bin(arr,i,0,n-1)
    if result == None:
        print(0,end=' ')
    else:
        print(1,end=' ')