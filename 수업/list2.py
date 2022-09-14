# N= int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N): #N = len(arr)
    for j in range(M):  #M = len(arr[0])
        print(arr[i][j], end=' ')
    print()