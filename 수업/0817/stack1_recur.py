##pypy에서 실행하면 된다.
def f(i, N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0,1000)