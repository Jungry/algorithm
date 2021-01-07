#1018번 체스판 다시 칠하기
n ,m = map(int,input().split())
data = []
result = []
for i in range(n):
    data.append(list(input()))

w = [['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W']]

b = [['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B'],
['B','W','B','W','B','W','B','W'],
['W','B','W','B','W','B','W','B']]

for i in range(n-7):
    for j in range(m-7):
        wr = 0
        br = 0
        for x in range(8):
            for y in range(8):
                if data[i+x][j+y] != w[x][y]:
                    wr += 1
                if data[i+x][j+y] != b[x][y]:
                    br += 1
        #print(wr,br)
        result.append(wr)
        result.append(br)

print(min(result))
#print(data)
#wr = 0
#br = 0
#for i in range(8):
#    for j in range(8):
#        if data[i][j] != w[i][j]:
#            wr += 1
#        if data[i][j] != b[i][j]:
#            br += 1
#result.append(wr)
#result.append(br)
#print(min(wr,br))
#