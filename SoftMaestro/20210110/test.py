fs = open('/Users/jungry/Desktop/vote1.txt','r',encoding='UTF-8-sig')

arr = [] 
while True:
    line = fs.readline()
    if len(line) == 0:
        break
    ele = line.split()
    arr.append(ele)

print(arr)