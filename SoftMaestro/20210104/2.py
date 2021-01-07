#럭키스트레이트

num = input()
num_l = num[:len(num)//2]
num_r = num[len(num)//2:]
result_l,result_r = 0,0

for i in range(len(num_l)):
    result_l += int(num_l[i])
    result_r += int(num_r[i])

if result_l == result_r:
    print('LUCKY')
else:
    print('READY')

