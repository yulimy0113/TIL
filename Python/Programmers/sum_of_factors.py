"""
https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
16'42"
"""

# My solution
import math

def solution(n):        
    answer = []
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(1, sqrt_n+1):
        if n % i == 0:
            answer.append(i)
            if n//i != sqrt_n:
                answer.append(n//i)
    return sum(answer)


# Best answer
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
