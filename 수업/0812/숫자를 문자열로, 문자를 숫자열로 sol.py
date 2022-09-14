# atoi => 문자열을 숫자로
print(ord('8')-ord('0')) #원리를 이용

def atoi(s):
    i = 0
    for char in s:
        i = i*10
        i += ord(char) - ord('0')
    return i

# itoa  => 숫자를 문자열로
# (단, 정수)

print(chr(0+ord('0')))

def itoa(num):


    #####0일 때 예외 처리
    if num == 0:
        return '0'

    #### 음수 양수 구분.
    is_positive = True
    if num <0:
        is_positive = False
        num = -num


    ans = ''  #만들어질 str을 넣을 녀석
    while num:
        # num, reminder = divmod(num, 10)  #몫과 나머지를 주는 함수
        num, reminder = num //10, num%10

        ans = (chr(reminder + ord('0'))) +ans  ##문자열인 한글자 짜리 숫자
    if is_positive:
        return ans
    else
        return '-' + ans

print(itoa(1351351))
print(type(itoa(1351351)))