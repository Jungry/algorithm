numbers = [0,1]
result = set([])

#print(result)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j :
            continue
        else:
            result.add(numbers[i]+numbers[j])
result = sorted(list(result))
print(result)