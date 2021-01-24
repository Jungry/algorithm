#9012 괄호

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    vps = input()
    result = 0
    for i in vps:
        #print(i)
        if i =='(':
            stack.append('(')
            #print(stack)
        elif i ==')':
            if stack: #스택에 값이 있다면
                stack.pop() #스택꺼 꺼내기
            else: #스택이 비었다면
                #print('work')
                result += 1
                break
    if stack:
        result += 1 #다 끝났는데 스택이 안빈경우
    if result >= 1:
        print('NO')
    else:
        print('YES')