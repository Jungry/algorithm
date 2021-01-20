import sys
def bin(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bin(arr,target,mid+1,end)
    else:
        return bin(arr,target,start,mid-1)
    
n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

m = int(sys.stdin.readline().rstrip())
check = list(map(int,sys.stdin.readline().rstrip().split()))

for i in check:
    result = bin(arr,i,0,n-1)
    if result == None:
        print(0)
    else:
        print(1)

def bin2(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return None

for i in check:
    result = bin2(arr,i,0,n-1)
    if result == None:
        print(0)
    else:
        print(1)
