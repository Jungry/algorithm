#좌표 정렬하기

#점 n의 개수 , 좌표가 n 개 주어진다  이것을 정렬하기

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]),int(input_data[1])))

array = sorted(array)

for i in range(n):
    print(array[i][0],array[i][1])