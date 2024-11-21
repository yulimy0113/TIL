"""
There are two arrays A, B with the same numbers of natural number.
Pick one number from each array and multiply them.
Repeat the process for the length of the array and add the product of two chosen numbers cumulatively.
Then,
Get the minimum cumulative sum.
(You cannot pick the number from the same position in the same array!)
"""


def solution(A,B):
    return sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))])
