
def preOrder(root):
    if root:
        print(str(root.info)+" ", end="") 
        preOrder(root.left)
        preOrder(root.right)



