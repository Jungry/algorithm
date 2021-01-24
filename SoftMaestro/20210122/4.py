#4949 균형잡힌 세상
import sys
input = sys.stdin.readline

match = {')':'(',']':'['}

while True:
    string = str(input().rstrip())
    stack = []
    check = 0

    if string =='.':
        break
    for word in string:
        #print(word)
        if word in '[(':
            stack.append(word)
        elif word in match:
            if not stack: #스택이 빈 경우
                print('no')
                check += 1
                break
            else:
                t = stack.pop()
                if t != match[word]:
                    print('no')
                    check += 1
                    break
    if stack and check == 0 : #스택이 비지 않은 경우
        print('no')
    elif not stack and check == 0 :
        print('yes')

