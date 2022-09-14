# 노드라는게 있다
# 왼쪽 오른쪽에 대한 무언가의 정보가 필요
#
# 구현하려면??
#
# 알고 있는 개념을 추상화 하여 구현하자
#
# 클래스를 사용

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

#0을 root node 로 설정
root_node = Node(0)
node_1 = Node(1)
node_2 = Node(2)

root_node.left = node_1   ###루트 노드의 왼쪽을 가르켜라.
node_1.parent = root_node

root_node.right = node_2

수도 코드

def func(node):
    if node ==None:
        실패
    if value == node.data:
        성공
    elif value < node.data:
        func(node.left)
    elif value > node.data:
        func(node.right)