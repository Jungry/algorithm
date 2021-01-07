#모험가 길드

n = int(input()) #모험가의 수
fright = list(map(int,input().split()))
count = 0
fright.sort()
high = fright[-1]
print(fright)

while True:
    fright = fright[0:-(high)]
    count += 1
    print(fright)
    if len(fright) == 0:
        break
    high = fright[-1]

print(count)


n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #그룹 개수
count = 0 #현재 그룹의 인원수

for i in data:
    count += 1
    if count >= i: #인원수가 충분하다면 
        result += 1
        count = 0
print(result)