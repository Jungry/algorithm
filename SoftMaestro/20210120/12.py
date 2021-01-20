#8979
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    inp = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(inp)

arr = sorted(arr,key = lambda x : (-x[1],-x[2],-x[3]))
x = 1
win = []
count= 0
for i in range(len(arr)-1):
    if arr[i][1:4] == arr[i+1][1:4]: #등수가 똑같은 경우
        win.append((arr[i][0],x))
        count += 1
    else:
        #print(arr[i+1])
        win.append((arr[i][0],x))
        x += count
        count = 0
        x+=1
if arr[-1][1:3] == arr[-2][1:3]:
    win.append((arr[-1][0],x))
else:
    win.append((arr[-1][0],(x)))
win = sorted(win,key=lambda x:x[0])
print(win[m-1][1])