#무지의 먹방 라이브

def solution(food_times,k):
    count = 0
    now_food = 0
    zero = 0

    while count != k:
        print('count : ',count)
        if food_times[now_food] != 0: #음식이 있는 경우
            count += 1
            food_times[now_food] -= 1
            now_food += 1
            zero = 0

            if now_food == len(food_times):
                now_food = 0
        elif food_times[now_food] == 0 :
            #print(zero)
            zero += 1
            now_food += 1

            if now_food == len(food_times):
                now_food = 0

            if zero == len(food_times):
                return -1
    for i in range(len(food_times)):
        print(now_food)
        if food_times[now_food] != 0:
            return now_food + 1
            
        else:
            now_food += 1

            if now_food == len(food_times):
                return -1
#

food_times = [1,1,1,1]
k = 2

print(solution(food_times,k))
