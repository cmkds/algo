def f(x,n):
    if n ==1:
        return x

    #이렇게 리스트나 딕셔너리에 넣어두면 예전거를 바로 쓸 수 있다.
    # lst[n//2] = f(x, n//2)
    # dic[n//2] = f(x, n//2)

    if n % 2:
        # return f(x, n//2)* f(x, n//2)*x
        half = f(x, n//2)
        return half * half * x

    else:
        half = f(x, n//2)
        return half * half