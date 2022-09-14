# lst = [1,1]
# for _ in range(50):
#     lst.append(lst[-1]+lst[-2])
# print(lst)

# memo = [1,1] #피보나치 수열을 담고 있는 리스트
n = 10
memo = [0]*(n)
memo[0] = 1
memo[1] = 1

def fibo(n):
    print(memo)
    if memo[n-1]:
        return memo[n-1]
    elif memo[n-1] ==0:
        memo[n-1] = fibo(n-1) + fibo(n-2)
        return memo[n-1]

print(fibo(n))

memo = [1,1]
for _ in range(n-2):
    memo.append(memo[-1] + memo[-2])
print(memo)