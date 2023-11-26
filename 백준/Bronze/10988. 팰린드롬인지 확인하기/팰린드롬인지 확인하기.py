s = list(input())
def palendrom(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return 0
    return 1
print(palendrom(s))
       