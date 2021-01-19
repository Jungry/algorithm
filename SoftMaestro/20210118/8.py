tc = int(input())
for x in range(tc):
    n = int(input())
    array = []
    for i in range(n):
        array.append(list(map(int,input().split())))
    array = sorted(array,key = lambda x : x[0])
    #print(array)
    maxx = array[0][1]
    num = 1
    
    for i in range(1,len(array)):
        if array[i][1]<maxx:
            num += 1
            maxx = array[i][1]
    print(num)