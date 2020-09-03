#나이순 정렬

n = int(input())

array = []

for _ in range(n):
    input_data = input().split()
    array.append((int(input_data[0]),input_data[1]))

array = sorted(array,key = lambda array : array[0])

for i in range(n):
    print(str(array[i][0]),array[i][1])