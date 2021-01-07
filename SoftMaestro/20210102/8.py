#1541 잃어버린 괄호
#생각 1 연속해서 두 개 이상의 연산자가 안나오니까 +에 다 괄호치기 

#55-(50+40)-(80+70)
#구현 어떻게 ?????
x = input().split('-')
num = [] #새 숫자가 들어갈 list
#print(x)
for i in x:
    count = 0
    sp = i.split('+')
    #print(sp)
    for j in sp:
        count += int(j)
    num.append(count)

result = num[0]
for j in range(1,len(num)):
    result -= num[j]
print(result)


######## 틀린거 ###########
x = input().split('-')
num = [] #새 숫자가 들어갈 list
#print(x)
for i in x:
    sp = i.split('+')
    #print(sp)
    if len(sp) >= 2:
        num.append(int(sp[0])+int(sp[1]))
    else:
        num.append(int(sp[0]))

result = num[0]
for j in range(1,len(num)):
    result -= num[j]
print(int(result))
