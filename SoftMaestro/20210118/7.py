#1541 잃어버린 괄호
array = list(map(str,input().split('-')))
new_arr = []
for i in array:
    count = 0
    sp = i.split('+')
    for j in sp:
        count += int(j)
    new_arr.append(count)

result = new_arr[0]
for i in new_arr[1:]:
    result -= i
print(result)

