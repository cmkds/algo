class Stack:

    def __init__(self,size):
        self.size = size
        self.data = [None]*size #양의 정수만 넣는다고 할 때는 0으로 초기화 해도 되는데
                                #다른 것을 넣을 경우 "비어 있다"를 표현하려면 None 이좋다.
                                #그러니까 None 으로 초기화 하자.
        self.top = -1   # -1이나 None 으로 잡아 놓고 갈 수도 있다.


    def push(self, value):
    #    if self.size == self.top + 1 :
        if self.is_full():
            print('가득찼어')
            raise
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            print('텅비었어')

        else:
            value = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.is_empty():
            print('비어있어')
        else:
            return self.data[self.top]


    def is_full(self):
        #1
        # if self.size == self.top +1:
        #     return True
        # else:
        #     return False
        # 2
        # return True if self.size == self.top +1 else False
        # 3
        return (self.top +1 == self.size)

    def is_empty(self):
        return (self.top == -1)

    def length(self):
        return self.top + 1

    def __str__(self):
        return f'{self.data}'

    # def __str__(self):
    #     for i in self.data[::-1]:
    #         if i is None:
    #             break
    #         else:
    #             print(i)

stack = Stack(3)
print(stack)

stack.push(1)
print(stack)

stack.push(2)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.push(1)
print(stack)