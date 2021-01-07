#거스름돈
#내가 만든 코드

n = 1260 #거스름돈
count = 0
money =[500,100,50,10]
for i in range(len(money)):
    count += n//money[i]
    n = n%money[i]
print(count)

#책의 코드
n = 1260
count = 0
money = [500,100,50,10]
for i in money:
    count += n//i
    n %= i
print(count)