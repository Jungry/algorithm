#부품 찾기
#특정한 수가 한번이라도 등장했는지 검사하는거라 set 쓰면 됨

n = int(input())
#전체 부품 번호를 받아서 set 에 저장
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end = ' ')
