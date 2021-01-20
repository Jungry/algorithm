#회의실 배정
import sys
n = int(sys.stdin.readline().rstrip())
time = []
for _ in range(n):
    time.append(list(map(int,sys.stdin.readline().rstrip().split())))
time = sorted(time,key =  lambda x:(x[1],x[0]))
total = 1
start = time[0]
for i in range(1,len(time)):
    if start[1] <= time[i][0]:
        total += 1
        start = time[i]
print(total)