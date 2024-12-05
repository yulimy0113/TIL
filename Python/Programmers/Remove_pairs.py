"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973
42'48"
"""


# My Answer : Not a right answer
def solution(s):
    init_len = len(s)
    while len(s) >= 2:
        for i in range(0, len(s) - 1):
            if (len(s) >= i) & (len(s) >= (i+2)):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
        if init_len == len(s):
            return 0
    if len(s) == 0:
        return 1
    elif len(s) != 0:
        return 0


# Best Solution
def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
        top = stack[-1]
        if top == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        return 1
    return 0
