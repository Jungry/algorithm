#체육복
def solution(n,lost,reverse):
    total = [1] * (n+1)
    for i in lost:
        total[i] -=1
    for i in reverse:
        total[i] += 1
    for i in range(1,len(total)-1):
        if total[i] == 0:
            if total[i-1] == 2:
                total[i-1]-=1
                total[i] += 1
            elif total[i+1] == 2:
                total[i+1] -= 1
                total[i] += 1
    
    count =-1
    for i in total:
        if i >= 1:
            count += 1
    return count

total = solution(5,[1,2,4,5],[2,3,4])
print(total)
