# JadenCase: Each word has its first letter in capital and the rest in lowercase.
# But, if the first letter is not alphabet, all the letters would be lowercase.
# Numbers can only be placed at the first position in each word.
# There is no word that consists of numbers only.
# There is a posibility that whitespaces come in a row.

def solution(s):
    """
    Return string s in JadenCase.
    s: string, length of s is longer than 1 and shorter than 200, s can contain alphabet, number, and whitespace.
    answer: list of words after JadenCase process.
    """
    answer = []
    for word in s.lower().split(" "):
        if len(word) >= 1:
            answer.append(word[0].upper()+word[1:])
        else:
            answer.append(word)
    return " ".join(answer)


# Other Solution
def Jaden_Case(s):
    return s.title()
