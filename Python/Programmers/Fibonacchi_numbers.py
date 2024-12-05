"""
https://school.programmers.co.kr/learn/courses/30/lessons/12945
11'19"
"""

# My Answer
def solution(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b%1234567  # it could be just "b" as the number 1234567 is big enough.
