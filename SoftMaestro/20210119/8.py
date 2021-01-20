#12015 가장 긴 증가하는 부분 수열 2
#DP 문제

import sys
n = int(sys.stdin.readline().rstrip())
arr= list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))