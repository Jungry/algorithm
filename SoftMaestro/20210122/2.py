#10799 쇠막대기
import sys
input = sys.stdin.readline

f = input()
stack = []
result = 0
for i in range(len(f)):
    print(f[i])
    if f[i] =='(':
        stack.append('(')
    elif f[i] == ')':
        if f[i-1] =='(':
            stack.pop()
            result += len(stack)
        elif f[i-1] ==')':
            stack.pop()
            result += 1
        
print(result)