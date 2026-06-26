from TreeNode import TreeNode

# inorder left->root ->right 
"""
Takes in a TreeNode and recurses through it and prints the tree in order
"""
def recursive_in_order(root): 
    if not root:
        return 
    recursive_in_order(root.left)
    print(root.val)
    recursive_in_order(root.right)

"""
Takes in a TreeNode and performs iterative inorder traversal and prints it 
"""
def iterative_in_order(root): 
    if not root:
        return
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left 
        curr = stack.pop()
        print(curr.val, ",")
        curr = curr.right 

# post order: left ->right->root 
def recursive_post_order(root): 
    if not root:
        return 
    recursive_post_order(root.left)
    recursive_post_order(root.right)
    print(root.val, end=", ")

def iterative_post_order(root): 
    last_visited = None 
    curr = root  
    stack = []
    while stack or curr: 
        while curr:
            stack.append(curr)
            curr = curr.left 
        curr = stack[-1]
        if curr.right and curr.right != last_visited:
            curr = curr.right 
        else:
            last_visited = stack.pop() 
            print(curr.val, ",")
            curr = None # We want to start from the top of the stack 

# pre-order: root->left->right 
# def recursive_pre_order(): 
def recursive_pre_order(root):
    if not root:
        return 
    print(root.val, end=", ")
    recursive_pre_order(root.left)
    recursive_pre_order(root.right)

# def iterative_pre_order(): 
"""
iterative pre_order
"""
def iterative_pre_order(root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr.val, end=", ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

if __name__ == "__main__":
    l = TreeNode(1,
    left=TreeNode(2,
        left=TreeNode(4),
        right=TreeNode(5)
    ),
    right=TreeNode(3,
        left=None,
        right=TreeNode(6)
    )
)
    iterative_in_order(l)