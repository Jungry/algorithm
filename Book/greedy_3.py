#숫자 카드 게임
n,m = map(int,input().split())
min_lst = []
result = 0

for i in range(n):
    card = list(map(int,input().split()))
    min_lst.append(min(card))

result = max(min_lst)
print(result)