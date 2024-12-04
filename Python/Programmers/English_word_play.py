"""
https://school.programmers.co.kr/learn/courses/30/lessons/12981
45'53"
"""
# My solution
def solution(n, words):
    words_played = [words[0]]
    for i, word in enumerate(words[1:]):
        len_play = i+2
        if word in words_played:
            return [n if len_play%n == 0 else len_play%n, len_play//n if len_play%n == 0 else (len_play//n+1)]
            
        elif word not in words_played:
            words_played.append(word)
            if words_played[i][-1] != word[0]:
                return [n if len_play%n == 0 else len_play%n, len_play//n if len_play%n == 0 else (len_play//n+1)]
                
    return [0,0]



# Best solution
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
