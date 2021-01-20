#11652 카드
import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr = sorted(arr)
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
arr = sorted(dic,key = lambda x: dic[x],reverse=True)
print(arr[0])