def Counting_Sort(A,B):
    ##A는 입력배열
    ##B는 정렬된 배열
    #C[]는 카운트 배열
    ###비교환 방식
    #평균 수행시간 O(n+k), O(n+k) 비교환 방식 n이 비교적 작을 때만 가능하다.

    C = [0] * len(A)

    for i in A:
        B[i] +=1

    for i in range(1,len(B)):
        B[i] += B[i-1]

    for i in range(len(A)-1,-1,-1):
        B[A[i]] -= 1
        C[B[A[i]]] = A[i]




A=[0,4,1,3,1,2,4,1]
B= [0]* len(set(A))

Counting_Sort(A,B)