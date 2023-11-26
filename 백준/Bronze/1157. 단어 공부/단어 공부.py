from collections import Counter
import sys
s = sys.stdin.readline().upper()
if len(s) == 2:
    print(s)
elif Counter(s).most_common()[0][1] == Counter(s).most_common()[1][1]:
    print("?")
else:
    print(Counter(s).most_common()[0][0])

