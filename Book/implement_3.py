#왕실의 나이트 (열과 행을 입력받아서 이동할 수 있는 방향들 찾기)

data = input()  #열과 행 입력
row = int(data[1]) #행
column = int(ord(data[0])) - int(ord('a')) +1 #소문자 a 를 숫자로 바꾸기 (열)

step = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(1,2),(-1,2),(-1,-2)]

result = 0

for i in step:
    next_row = row + i[0]
    next_column = column + i[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
