#10816 숫자카드 2
import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
num = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
dic = {}
for i in num:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
#print(dic)
m = int(sys.stdin.readline().rstrip())
get_num = list(map(int,sys.stdin.readline().rstrip().split()))

#counter =Counter(num)
#
#for i in get_num:
#    print(counter[i],end=' ')
#

for i in get_num:
    if i not in dic:
        print(0,end=' ')
    else:
        print(dic[i],end=' ')

