a = int(input())

if a % 6 == 0:
    res = (((a // 6) + 1) * ((a // 6) * 3)) + 1
else:

    res = ((a // 6) + 1) * (((a // 6) * 3) + a % 6)
print(res%1000000)