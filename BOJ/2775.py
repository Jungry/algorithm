#부녀회장이 될테야

num = int(input())
for _ in range(num):
    array = [x for x in range(1,15)]
    k= int(input())
    n = int(input())
    for i in range(k):
        for j in range(n):
            if j == 0:
                continue
            else:
                array[j] = array[j-1]+array[j]

    print(array[n-1])