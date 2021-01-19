n = input()

arr = []
for i in range(len(n)):
    arr.append((i,int(n[i])))
arr = sorted(arr,key = lambda x: x[1])
for _ in range(2):
    del arr[0]
arr = sorted(arr)
result = ''
for i in arr:
    result += str(i[1])
print(type(result))