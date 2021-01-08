#print((ord('')-ord('A'))%13)\
string = 'AAA'
count = 0
#오른쪽으로 가는 경우
for i in range(len(string)):
    now_string = 'A'*len(string)
    if now_string == string:
        break
    if ord(i)-ord('A') <= 13: #A-N
        print((ord(i)-ord('A')))
        count += (ord(i)-ord('A'))
        now_string[i]
    elif ord(i)-ord('A') > 13:
        print(13-(ord(i)-ord('A'))%13)
        count += 13-(ord(i)-ord('A'))%13

print(count)

