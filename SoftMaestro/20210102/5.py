#문자열 뒤집기
#처음에 생각한 풀이 : 1->0 혹은 0->1 로 변하는 부분의 개수 나누기 2를 해주자 !! 틀림 ㅜㅜ

num = input()
result = 0
for i in range(len(num)-1):
    if num[i] != num[i+1]:
        result +=1
print(result//2)

#전부 0으로 바꾸는거랑 전부 1로 바꾸는거 둘다 구해서 비교하기

data = input()
count0 = 0
count1 = 0

if data[0] == '1': #0으로 만드는 경우
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else: 
            count1 += 1
print(min(count0,count1))
