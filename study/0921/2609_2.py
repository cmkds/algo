def yaksoo(n, lst):                              ##약수 집합을 구하는 함수를 만들었다.
    for i in range(1,n//2+1):                    ##1부터 n//2 까지 약수 구한다.
        if n%i == 0:
            lst.append(i)
    lst.append(n)               ########for문 반절줄이려고 n//2+1로 했는데 자기자신을 리스트에 안넣어서 43%인가에서 틀림
    return lst

a, b = map(int,input().split())

lstA =[]
lstB= []

yaksoo(a,lstA)
yaksoo(b,lstB)
print(lstA)
print(lstB)
#[2, 3, 4, 6, 8, 12] [2, 3, 6, 9] 약수의 집합을 다 찾아준다.


kyoZipHap = list(set(lstA) & set(lstB))
#####셋 배울 때 배웠던 교집합
# print(kyoZipHap)       ###### [2, 3, 6]

print(max(kyoZipHap))         ########이놈이 최대공약수
print(a*b//(max(kyoZipHap)))  #최고공배수는 두수의 곱 /최대공약수이다.

