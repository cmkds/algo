arr = [1,2,3,4,5]

n = len(arr)
res = []  #전체가 들어갈 녀석
for i in range(2**n):
    tmp_lst = []  #개별적인 0000, 0001, 1101 ~~~등등에 대한 리스트가 들어갈 녀석
    for j in range(n):
        if i & (1<<j):  ## 해당하는 리스트들을 tmp_lst에 넣는 과정
            tmp_lst.append(arr[j])
    res.append(tmp_lst)

print(res)