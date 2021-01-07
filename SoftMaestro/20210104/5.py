num = int(input())
answer = 0

for i in range(1,num+1):
    c_list = list(map(int,str(i))) #각 자리수 짤라서 list에 넣기
    answer = i+sum(c_list)

    if answer == num:
        print(i)
        break
    if i == num:
        print(0)