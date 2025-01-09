"""
Lv.1 Make a Weird Word
https://school.programmers.co.kr/learn/courses/30/lessons/12930
7'38"
"""

# My Answer
def solution(s):
    words_list = s.split(' ')
    answer = []
    for word in words_list:
        for i in range(len(word)):
            if i%2:
                word = word[:i] + word[i].lower() + word[i+1:]
            else:
                word = word[:i] + word[i].upper() + word[i+1:]
        answer.append(word)
    return " ".join(answer)



# Best Solution
def solution(s):
  return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.uppwer() for i, a in enumerate(x)]), s.split(" ")))
