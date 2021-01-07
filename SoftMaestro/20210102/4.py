#곱하기 혹은 더하기
#result 가 0이나 1인경우 +
#num 이 0 이나 1인경우 +
#나머지 경우 *
num = input()
result = 0
for i in num:
    if result == 0 or result == 1 :
        result += int(i)
    elif i == 1 or 1 == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)

#책의 풀이
data = input()

result = int(data[0])
for i in range(1,len(data)):
    num =int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

