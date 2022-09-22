a, b = map(int,input().split())

lstA =[]
lstB= []
# 2~n//2
def yaksoo(n,lst): ##약수 집합을 구하는 함수를 만들었다.
    for i in range(2,n//2+1):
        if n%i ==0:
            lst.append(i)
    return lst

yaksoo(a,lstA)
yaksoo(b,lstB)

#print(lstA,lstB)
#[2, 3, 4, 6, 8, 12] [2, 3, 6, 9] 약수의 집합을 다 찾아준다.

kyoZipHap = list(set(lstA) & set(lstB))    #####셋 배울 때 배웠던 교집합
# print(kyoZipHap)                      ####### [2, 3, 6]

print(max(kyoZipHap))########이놈이 최대공약수

#최고공배수는 두수의 곱 /최대공약수이다.

print(a*b//(max(kyoZipHap)))

