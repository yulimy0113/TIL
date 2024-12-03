"""
https://school.programmers.co.kr/learn/courses/30/lessons/12924
23'11"
"""

# My Answer
def solution(n):
    dividors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dividors.append(i)
            if i != (n // i):
                dividors.append(n // i)
    return len([ans for ans in dividors if ans % 2 != 0])


# Best Solution
def expressions(num):
    return len([i for i in range(1, num + 1, 2) if num % i == 0])
