#수 찾기
import sys

n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

m = int(sys.stdin.readline().rstrip())
check = list(map(int,sys.stdin.readline().rstrip().split()))

def bin(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target :
        return bin(array,target,start,mid-1)
    else:
        return bin(array,target,mid+1,end)

for i in check:
    re = bin(arr,i,0,n-1)
    if re == None:
        print(0)
    else:
        print(1)