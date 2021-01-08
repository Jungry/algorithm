height = []
for _ in range(9):
    height.append(int(input()))
height.sort()
total = sum(height)
fake = total-100

for i in range(len(height)-1):
    for j in range(i,len(height)):
        if (height[i]+height[j]) == fake and i!=j:
            #print(i,j)
            height.pop(j)
            height.pop(i)
            break

for i in height:
    print(i)
