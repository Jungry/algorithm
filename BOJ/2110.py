#공유기 설치 (아직 다 못함)

n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))

start = min(array)
end = max(array)

while start <= end:
    total = 0
