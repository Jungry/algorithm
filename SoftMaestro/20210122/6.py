#1918번 후위표기식
import sys
input = sys.stdin.readline
sick = input().rstrip()

stack = []
result = ''

for i in sick:
    if i in '+-*/':
        stack.append(i)
    elif i == '(':
        continue
    elif i == ')':
        if stack:
            t = stack.pop()
            result += t
    else:
        result += i

if stack:
    for _ in range(len(stack)):
        t = stack.pop()
        result += t
print(result)
