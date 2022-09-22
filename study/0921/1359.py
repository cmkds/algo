from itertools import combinations       ###원하는 길이의 부분집을 가져오기 위해서 콤비네이션을 사용했다.



N, M, K = map(int,input().split())   #N M K # 1~N 까지 수 M개 고르기 적어도 K개 같기

lst = list(i for i in range(1,N+1))   ### 1~N까지 리스트 한번에 만들기

a = list(combinations(lst,M))        ### M길이의 부분집합 전부 추출.
#print(a)  [(1,), (2,), (3,)]

chk = a[0]                  ##나는 무조건 첫번째 부분집합을 뽑았다고 생각하고
                            ##주최자는 순서대로 처음부터 끝까지 뽑았다고 가정한 후
                            ##확률을 계산했다.
                            ##내가 뭘 뽑든 확률은 같으니까. 이렇게 해도 된다.

cnt = 0
for aa in a:                ##aa = N개중에 M개 뽑는 경우의 수중 하나
    tmpCnt = 0
    for aaa in aa:          ##aa의 원소들이 chk에 있는지 하나하나 비교한다.
        if aaa in chk:
            tmpCnt +=1      ##비교하면서 chk안에 있으면 tmpCnt 증가

    if tmpCnt >=K:          ## tmpCnt가  K보다 넘었을 시 cnt를 1증가
        cnt +=1

print(cnt/len(a))           ## 겹치는게 K개가 넘은 경우/전체 경우의 수