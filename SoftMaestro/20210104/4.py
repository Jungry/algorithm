#블랙잭 
#완전 탐색

n,m = map(int,input().split())
card = list(map(int,input().split()))

card.sort()
curr_card = 0
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            new_card = card[i]+card[j]+card[k]
            #print(new_card)
            if new_card <= m and curr_card <= new_card:
                curr_card = new_card
                #print(card[i],card[j],card[k])
print(curr_card)
