import sys


def extreme_split(s):
    arr = []
    for i in range(len(s) - 3):
        arr.append(s[i] + s[i + 1] + s[i + 2])
    return arr


def countAns(s, word):
    if len(s.split(word)) - 1 != 1:
        return len(s.split(word)) - 1
    else:
        return 0


def validAns(setA, ans):
    finallyAns = [[], []]

    for i in range(len(ans)):
        if ans[i] != 0:
            finallyAns[0].append(setA[i])
            finallyAns[1].append(ans[i])

    if len(finallyAns[0]) == 0:
        return [[], [0]]
    return finallyAns


ans = []


for line in sys.stdin:
    setA = sorted(list(set(extreme_split(line))))
    for word in setA:
        ans.append(countAns(line, word))
    print(validAns(setA, ans))
    setA = []
    ans = []