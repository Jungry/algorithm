#10826 스택
import sys
input = sys.stdin.rstrip().readline

def push(n,stack):
    stack.append(n)
def pop(stack):
    if len(stack) ==0:
        print(-1)
    else:
        print(stack.pop())
def size(stack):
    print(len(stack))
def empty(stack):
    if len(stack) == 0:
        print(0)
    else:
        print(1)
def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

stack = []
n = int(input())
for _ in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        push(int(arr[1]),stack)
    elif arr[0] == 'pop':
        pop(stack)
    elif arr[0] == 'size':
        size(stack)
    elif arr[0] == 'empty':
        empty(stack)
    elif arr[0] == 'top':
        top(stack)
    
    
