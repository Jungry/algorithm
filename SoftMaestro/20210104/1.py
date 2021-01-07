curr = input()
row = int(curr[1]) #앞에꺼 
column = int(ord(curr[0])) - int(ord('a')) + 1 #뒤에꺼

steps = [(1,-2),(-1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,-1),(-2,1)]

result = 0

for i in steps:
    new_row = row +i[0]
    new_col = column + i[1]

    if new_row >= 1 and new_row <= 8 and new_col >=1 and new_col <= 8:
        result += 1
print(result)