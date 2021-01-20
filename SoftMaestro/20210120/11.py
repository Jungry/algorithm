#1157 단어 공부
import sys
from collections import Counter

s = list(sys.stdin.readline().rstrip().lower())
if len(s) == 1:
    print(s[0].upper())
else:
    s = Counter(s).most_common(2)
    if s[0][1] == s[1][1]: #길이가 같으
        print('?')
    else:
        print(s[0][0].upper())
