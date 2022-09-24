def preorder(T):
    if T:
        visit(T)
        preorder(T.left)
        preorder(T.right)

def inorder(T):
    if T:
        inorder(T.left)
        visit(T)
        inorder(T.right)

def postorder(T):
    if T:
        postorder(T.left)
        postorder(T.right)
        visit(T)