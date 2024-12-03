# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(num):
  """
  Return a list of number of repetition and numbers of zero that was removed from the initial input.
  num: string, binary number array
  """
    zeros = 0
    rep = 0
    while num != '1':
        zeros += (len(num) - len(num.replace("0", "")))
        num = bin(len(num.replace("0", "")))[2:]
        rep += 1
    return [rep, zeros]
