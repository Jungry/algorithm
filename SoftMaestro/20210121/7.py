#1874 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
cur = 1 #시작은 1

stack = []

num_list = []
num_count = 0
for _ in range(n):
    num_list.append(int(input()))
ans = 1
lst = []
while n > num_count:
    if stack: #스택이 비지 않았을때
        if stack[-1] != num_list[num_count]:
            if cur > num_list[num_count]:
                ans = 0
                print('NO')
                break
            else:
                stack.append(cur)
                lst.append('+')
                cur += 1
        elif stack[-1] == num_list[num_count]:
            lst.append('-')
            num_count += 1
            stack.pop()
    else: #스택이 빈경우
        stack.append(cur)
        lst.append('+')
        cur += 1

if ans != 0:
    for i in lst:
        print(i)
    