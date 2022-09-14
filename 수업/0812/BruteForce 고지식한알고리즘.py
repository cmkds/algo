text = 'this is book'
pattern = 'is'

    #i 는 텍스트를 반복하는 녀석
def func(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)): ##패턴을 반복하는 녀석
            if text[i+j] != pattern[j]:
                break
        else:
            return i
    return -1

def func2(text, pattern):
    m = len(pattern)
    for i in range(len(text)- len(pattern)+1):
        if text[i:i+m] == pattern:
            return i
    return -1


def func3(text, pattern):
    i = 0     #i는 전체 텍스트
    j = 0     #j는 검사할 패턴
    M = len(pattern)
    N = len(text)

    while j < M and i < N:
        if text[i] != pattern[j]:
            i = i-j
            j = -1
        i = i +1
        j = j +1
    if j == len(pattern):
        return i-len(pattern)
    else:
        return -1

