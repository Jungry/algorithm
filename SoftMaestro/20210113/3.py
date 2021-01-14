#부품 찾기 (3 set 사용)
import timeit

n = int(input())
array = set(map(int,input().split()))

m = int(input())
data = list(map(int,input().split()))

start_time = timeit.default_timer()

for i in data:
    if i in array:
        print('YES',end=' ')
    else:
        print('NO',end=' ')

end_time = timeit.default_timer()
print('%f초 걸렸습니다.'%(end_time-start_time))


n = int(input())
array = list(map(int,input().split()))

m = int(input())
data = list(map(int,input().split()))

start_time = timeit.default_timer()

for i in data:
    if i in array:
        print('YES',end=' ')
    else:
        print('NO',end=' ')

end_time = timeit.default_timer()
print('%f초 걸렸습니다.'%(end_time-start_time))

