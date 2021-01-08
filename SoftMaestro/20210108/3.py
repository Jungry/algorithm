#1181 단어 정렬

n = int(input())
array = []
for i in range(n):
    word = input()
    word_len = len(word)
    array.append((word_len,word))

array = set(array)
array = sorted(array,key=lambda x: (x[0],x[1]))


for i in array:
    print(i[1])