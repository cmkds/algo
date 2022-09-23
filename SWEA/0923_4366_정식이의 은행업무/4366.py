import sys
sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1,testNum+1):
    ei = list(input())
    sam = list(input())

    # print(ei, sam)

    setEi = set()
    setSam = set()
### 리스트 ei의 길이 만큼  for문돌리면서 숫자 바꾸기.
    for i in range(len(ei)):
        if ei[i] == '1':
            ei[i] = '0'
            a = int(''.join(ei), 2)
            setEi.add(a)
            ei[i] ='1'
        else:
            ei[i] = '1'
            a = int(''.join(ei), 2)
            setEi.add(a)
            ei[i] = '0'
    # print(setEi)

    for i in range(len(sam)):
        if sam[i] == '2':
            sam[i] = '1'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] = '0'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] ='2'

        elif sam[i] == '1':
            sam[i] = '2'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] = '0'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] = '1'

        else:
            sam[i] = '2'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] = '1'
            a = int(''.join(sam), 3)
            setSam.add(a)

            sam[i] = '0'
    # print(setSam)
    print(f'#{test} {list(setSam&setEi)[0]}')