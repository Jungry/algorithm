#선택정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index],array[i] #두개의 자리를 바꿔준다

print(array)

#삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): #i부터 서서히 감소하는 문법
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break
print(array)

#퀵 정렬

array =[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈린 경우
            array[right],array[pivot] = array[pivot],array[right]
        else:
            array[left],array[right] = array[right],array[left]
    
    quick_sort(array,0,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬의 장점을 살린 퀵 정렬 (조금 더 시간이 오래 걸리지만 직관적임)

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x<=pivot] #왼쪽 부분
    right_side = [x for x in tail if x > pivot] #오른쪽 부분
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) #분할 이후 각각 정렬을 수행

print(quick_sort(array))

#계수정렬

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1) #+1을 해주는건 0-9까지 총 10개니까
for i in range(len(array)):
    count[array[i]] +=1 
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

