def f(i, k):
    if i == k: # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]
N = 3
p = [i for i in range(1, N+1)]

# p = [1,2,3,4,5]
f(0, N)