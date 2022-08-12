# atoi => 문자열을 숫자로
# itoa  => 숫자를 문자열로
# (단, 정수)

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i
########################
def itoa(int):
    test = int
    cnt = 0
    while test >= 1:
        test /= 10
        cnt +=1
    ##cnt = 3
    while cnt !=0:
        k = test%(10**(cnt-1))
        print(k)
        cnt -= 1
    return cnt
    # for x in s:
    #     i = i*10 + ord(x)-ord('0')
    # return i
#############################


print(atoi('123'))
print(itoa(123))