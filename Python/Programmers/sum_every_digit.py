"""
https://school.programmers.co.kr/learn/courses/30/lessons/12931
1'48"
"""

def solution(n):
    return sum(list(map(lambda x: int(x), list(str(n)))))
