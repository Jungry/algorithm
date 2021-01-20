#2108 통계학
import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = sorted(arr)

#1
total = int(round(sum(arr)/n,0))
print(total)

#2
mid = len(arr)//2
print(arr[mid])

#3
if len(arr) >1:
    most_common = (Counter(arr).most_common(n=2))
    if most_common[0][1] == most_common[1][1]:
        print(most_common[1][0])
    else:
        print(most_common[0][0])
else:
    print(arr[0])
#4
print(arr[-1]-arr[0])