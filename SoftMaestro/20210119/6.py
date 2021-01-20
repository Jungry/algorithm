import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
no_listen = []
no_see = []
for _ in range(n):
    no_listen.append(sys.stdin.readline().rstrip())
for _ in range(m):
    no_see.append(sys.stdin.readline().rstrip())

no_listen = set(sorted(no_listen))
result = 0
no_ls = []
for i in no_see:
    if i in no_listen:
        result += 1
        no_ls.append(i)
    else:
        continue
print(result)
for i in no_ls:
    print(i)