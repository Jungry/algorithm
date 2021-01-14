#부품 찾기(1 이진탐색)

import sys

n = int(sys.stdin.readline().rstrip())
data =sorted(list(map(int,sys.stdin.readline().rstrip().split())))

m = int(sys.stdin.readline().rstrip())
bring = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

def bin(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin(array,target,start,mid-1)
    else:
        return bin(array,target,mid+1,end)

for i in bring:
    result = bin(data,i,0,n-1) 
    if result == None:
        print('NO',end=' ')
    else:
        print('YES',end=' ')
