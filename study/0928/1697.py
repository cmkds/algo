from collections import deque

def bfs():
    q = deque()                          ##큐로 넣어요
    q.append(start)                     ##시작값을 넣어요
    while q:                            ##큐가 빌때까지 와일문이 돌아요
        a = q.popleft()                 ##가장왼쪽값을 뽑아요.
        if a == end:                    ##도착점에 도착하면 while문을 끝내요.
            print(visited[end])
            break
        for nextA in (a - 1, a + 1, a * 2):    ##한단계를 지나갈때마다 기존칸에서 -1,+1,*2 의 칸을 추가해요.
                                               ##단계가 늘수록 3^n 개 만큼 케이스가 늘어나겠네여.
                                            ##케이스가 늘어나지만 visited[nx]에서
                                            ##방문했을시 안가기 때문에
                                            ## 조금은 줄겠지..요
            if 0 <= nextA <= 10 ** 5 and not visited[nextA]:  ##nx가 범위를 벗어나거나 방문했다면
                                                        ##안감.
                                                        ##not visited 여기서
                                                        ##bfs기때문에
                                                        ##이전에 방문한 값이있다면
                                                        ##무조건 지금 방문순서보단
                                                        ##낮기때문에
                                                        ##그 낮은 값으로 사용하는게
                                                        ##맞으니깐
                                                        ##뒤에 도착한값은
                                                        ##필요가 없다. 이것도 dp인가


                visited[nextA] = visited[a]+1     ##처음가는 점이면 visited에 이전 방문레벨+1의 값을 넣어준다.
                q.append(nextA)                   ##그리고 현재 방문위치를 큐에 넣어준다.

start,end = map(int,input().split())
visited = [0] * (10**5+1)                       ##visited리스트를 0<=  <=100000 으로 미리 만들어준다.
bfs()