#거스름돈 - greedy

money = int(input())
count = 0
coins = [500,100,50,10]

for i in coins:
    count += money // i
    money %= i

print(count)