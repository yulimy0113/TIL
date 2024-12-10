"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127
"""

# My Answer
from collections import Counter
def solution(want, number, discount):
    want_dict = {key: val for key, val in zip(want, number)}
    answer = 0
    
    for i in range(len(discount)-9):
        disc_10 = Counter(discount[i:i+10])
        if dict(disc_10) == want_dict:
            answer += 1
    return answer


