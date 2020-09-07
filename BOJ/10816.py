#숫자카드 2
array = [0] * 20000001

n = int(input())
card = list(map(int,input().split()))
m = int(input())
answer = list(map(int,input().split()))
for i in card:
    array[i] += 1
for x in answer:
    print(array[x],end=' ')