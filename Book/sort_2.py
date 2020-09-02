#성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []
for _ in range(n):
    input_data = input().split()
    #!!! 학생 정보를 (점수,이름) 으로 묶어줄 수 있다 !!!! 
    array.append((input_data[0],int(input_data[1])))

array = sorted(array,key = lambda array : array[1]) #[1] 기준으로 정렬

for student in array:
    print(student[0],end = ' ')