#5585 거스름돈
n = int(input())
coins = [500,100,50,10,5,1]
paid = 1000-n
total = 0

for i in coins:
    if paid // i > 0:
        total += paid//i
        paid = paid%i

print(total)