"""
Lv.2 Next Big Number
https://school.programmers.co.kr/learn/courses/30/lessons/12911
28'23"
"""

def solution(n):
    bin_n = format(n, 'b')
    num_n = bin_n.count('1')
    big_n = '1' * (len(bin_n) + 1)
    for num in range(n+1, int(f'0b{big_n}', 2)):
        if format(num, 'b').count('1') == num_n:
            return num
