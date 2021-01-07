s = "a"

def solution(s):
    word = []
    length = []
    for x in range(1,len(s)//2+2):
        word = []
        count = 1
        new = ''
        word = [s[i:i+x] for i in range(0,len(s),x)]
        #print(word)
        #if len(s)%x == 0:
        #    print('work')
        #    start = 0
        #    for _ in range(len(s)//x):
        #        word.append(s[start:start+x])
        #        start = start+x
        for z in range(len(word)-1):
            #print(z)
            #print(word[z])
            if word[z] == word[z+1]:
                count += 1
            elif word[z] != word[z+1]:
                if count > 1:
                    new += str(count)+word[z]
                    count = 1
                elif count == 1:
                    new += word[z]
        if count >1 :
            new += str(count)+word[-1]
        elif count == 1:
            new += word[-1]
        #print(new)
        #print(word)
        length.append(len(new))
    return min(length)
    #print(min(length))

s = "a"
print(solution(s))
