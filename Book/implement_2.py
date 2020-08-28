#시각 0시 부터 hour 시 까지 3 이 몇번 들어가는지 !
hour = int(input())
count = 0

for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1

print(count)