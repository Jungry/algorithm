def fibo(n):
    if n == 0 :
        print('work0')
        arr[0] += 1
        return 0
    if n == 1:
        print('work1')
        arr[1] += 1
        return 1
    else:
        print(n)
        return fibo(n-1)+fibo(n-2)

n = int(input())
for i in range(n):
    arr=[0,0]
    num = int(input())
    fibo(num)
    print(arr[0],arr[1])

