#좌표 정렬하기 2

n = int(input())

array = []
for _ in range(n):
    input_data = input().split()
    array.append((int(input_data[0]),int(input_data[1])))

array = sorted(array)
array = sorted(array,key = lambda array : array[1])

for i in range(n):
    print(array[i][0],array[i][1])