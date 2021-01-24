#2493 탑
import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
index = []
for i in range(len(top)):
    index.append((i,top[i]))

stack = []
result = []
for i in range(n):
    while stack:
        if stack[-1][1] > index[i][1]: #송신이 가능
            result.append(stack[-1][0]+1)
            stack.append(index[i])
            break
        else:
            stack.pop()
    if not stack: #스택이 비어서 송신 불가능
        result.append(0)
        stack.append(index[i])

for i in result:
    print(i,end=' ')
    