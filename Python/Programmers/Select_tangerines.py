"""
https://school.programmers.co.kr/learn/courses/30/lessons/138476
49'19"
"""

# My Answer: failed to solve it without using Counter
def solution(k, tangerine):
    tan_types = list(dict.fromkeys(sorted(tangerine, key = lambda x: tangerine.count(x), reverse=True)))
    num = 0
    for i, type in enumerate(tan_types):
        if num < k:
            num += tangerine.count(type)
        else:
            return i


# Best Solution
from collections import Counter
def solution(k, tangerine):
    types = 0
    cnt = Counter(tangerine)

    for item, count in cnt.most_common():
        k -= count
        types += 1
        if k <= 0:
            return types
