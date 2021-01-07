#11399 ATM
#인출할때 시간이 적게 소요되는 사람 순서로 줄을 세우면 된다

n = int(input())
p = list(map(int,input().split()))

p.sort()
total = 0 #총 기다린 시간
wait = 0 #개인이 기다린 시간

for i in p:
    wait += i
    total += wait
print(total)