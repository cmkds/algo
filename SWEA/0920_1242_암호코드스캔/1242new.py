import sys
sys.stdin = open('input.txt')


tc = int(input())

for idx in range(1, 11):
    n, m = map(int, input().split())    # 세로 크기 n, 가로 크기 m
    arr = list([input() for _ in range(n)])    # 중복제거
    print(arr)
    arr = sorted(arr)[0:]   # 0만 있는 배열 제거
    print(len(arr))
    print('##################################################################')
    # lst = set()
    print(arr)
    # for i in range(len(arr)-1):
    #     a = ''
    #     for j in range(m-1):
    #         if arr[i][j] != arr[i+1][j]:
    #             a += arr[i+1][j]
    #     lst.append(a)
    # print('@@@@@')
    # print(lst)
    # print('@@@@')
    # for i in range(len(arr)):
    #     arr[i] = arr[i].strip('0')
    #
    # #print(list(set(arr)))
    #
    # lst = list(set())
    # for i in arr:
    #     if not len(i)%14:
    #         lst.append(i)
    # print(lst)
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


    # for i in range(len(lst)):
    #     if '000000000000000000' in lst[i]:
    #         del lst[i]
    # print(lst)

#     numbers = []    # 암호 넣는 리스트
#     answer = 0
#     for p in arr:
# # 1. 16진수 -> 2진수 변환
# # 2. 왼쪽 0 다 제거
# # 3. 마지막에 0 붙이기 (마지막 자리를 위해)
#         binary = format(int(p, 16), 'b').lstrip('0') + '0'
#         #print(binary)
#         n1 = n2 = n3 = 0    # 각 비율을 담을 변수
#         cnt = 0  # 암호 8자리 count
#         odd = 0  # 홀수 자리 합 저장
#         even = 0  # 짝수 자리 합 저장

