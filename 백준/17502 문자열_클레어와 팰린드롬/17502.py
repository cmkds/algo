import sys
sys.stdin = open('input.txt')

#어차피 소문자로 주어져서 따로 소문자로 명시할 필요는 없다.
num = int(input())
#리스트 인풋을 하면 한개씩 리스트에 쏙쏙 들어가더라.
str = list(input())
print(num//2)
for idx in range(1 , (num//2)+1):
    while True:
        # 양쪽이 ?인 경우가 가장먼저
        if str[idx-1] == '?' and str[num-idx] == '?':
            str[idx-1] = str[num-idx] = 'a'
            break
        #양쪽이 같은 경우
        elif str[idx-1] == str[num-idx]:
            break
        #그다음이 양쪽다 ?인 경우가 가장먼저

        #한쪽만 ? 인 경우
        elif str[idx-1] == '?':
            str[idx - 1] = str[num-idx]
            break
        elif str[num-idx] == '?':
            str[num - idx] = str[idx - 1]
            break


##홀수 일 때 가운데 글자가 ? 라면 추가하니까 정답.
if str[num//2] == '?':
    str[num // 2] = 'a'





print(''.join(str))
