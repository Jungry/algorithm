n = int(input())
result = 0 
while True:
    if n%5==0: #5kg로 나누어 떨어지는 경우
        result += n//5
        break
    if n == 3:
        result += 1
        break
    n -= 3
    result += 1
    if n<= 2:
        result = -1
        break

print(result)