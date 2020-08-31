#ATM

people = int(input())
time = list(map(int,input().split()))

time.sort()

result = 0

for i in range(people):
    count = 0
    for j in range(0,i+1):
        count += time[j]
    result += count

print(result)
