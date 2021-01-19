#11399 ATM

n = int(input())
person = list(map(int,input().split()))
person = sorted(person)
now = 0
wait = 0
for i in range(n):
    now = now + person[i]
    wait += now

print(wait)