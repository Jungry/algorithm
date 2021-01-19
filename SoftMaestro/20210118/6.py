n = int(input())
array = []

for i in range(n):
    array.append(int(input()))
array.sort()
re_arr =[]
for i in array:
    re_arr.append(i*n)
    n-=1
print(max(re_arr))