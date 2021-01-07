#공유기 설치 (아직 다 못함)

n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array)
start = min(array)
end = max(array)

while start <= end:
    total = 0
    mid = (start+ end)//2

    if 
