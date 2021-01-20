#10815 숫자카드

n = int(input())
num = set(map(int,input().split()))
m = int(input())
get_num = list(map(int,input().split()))

for i in get_num:
    if i in num:
        print(1,end=' ')
    else:
        print(0,end=' ')

num = sorted(num)

def bin(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for i in get_num:
    re = bin(num,i,0,n-1)
    if re == None:
        print(0,end=' ')
    else:
        print(1,end=' ')
