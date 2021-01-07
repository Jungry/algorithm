#문자열 재정렬

string = input()
alpha = []
value = 0

for i in string:
    if i.isalpha():
        alpha.append(i)
        print(i)
    else:
        value += int(i)

alpha.sort()

if value != 0:
    alpha.append(str(value))

print(''.join(alpha))
