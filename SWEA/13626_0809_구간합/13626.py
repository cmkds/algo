import sys

sys.stdin = open('input.txt')

# def maxn(N,M,lst):
#     total = -999999999999999999999999999999999999999999
#     ##이중 포문을 둘려서 리스트의 합을내야된다.
#
#     for idx, tmp in enumerate(lst):
#         tmpTotal = 0
#         for _ in range(-M+idx, M+idx+1):
#             try :
#                 tmpTotal += lst[_]
#             except IndexError:
#                 break
#         if tmpTotal> total:
#             total = tmpTotal
#     return total


def maxn(N,M,lst):
    total = -999999999999999999999999999999999999999999

    for idx in range(N):
        tmpTotal = 0
        for i in range(-(M//2)+idx, (M//2)+idx+1):
            if i < 0 or i > N:
                print('예외!')
                ##tmpTotal을 0으로 만들고 싶은데
                ##tmpTotal = 0 은 안먹음.
                break
            try :
                tmpTotal += lst[i]
            except IndexError:
                print('예외')

                tmpTotal =0
                print(tmpTotal)
                break
        else:
            if tmpTotal > total:
                total = tmpTotal
    return total

def minn(N,M,lst):
    total = 9999999999999999999999999999999999999999999999999999999
    ##이중 포문을 둘려서 리스트의 합을내야된다.

    for idx in range(N):
        tmpTotal = 0
        for i in range(-(M//2)+idx, (M//2)+idx+1):
            try :
                tmpTotal += lst[i]
            except IndexError:
                tmpTotal = 0
                break
        else:
            if tmpTotal < total:
                total = tmpTotal
    return total


#구간의 갯수 //2 한 부분부터 시작한다.
#첫구간의 합을 첫변수로 저장.
#그 다음 변수부터는 대소를 비교한다.
#for문은 리스트 길이에서 M //2 만큼 양쪽에서 뺀다.


testNum = int(input())

for test in range(1, testNum+1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    print(f'#{test} {maxn(N,M,lst)-minn(N,M,lst)}')
