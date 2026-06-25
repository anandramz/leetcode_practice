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
# def recursive_post_order(): 
def iterative_post_order(root): 
    # Implementation Plan:
        # last visited, stack, curr 
        # 1. while stack or curr:
            # 2. while current is none null and not equal to top of the stack
                # check for case where stack length is not null
                # add current to stack and move current to left
            # 3. peak at the top of the stack 
            # 4. check if the top of the stack right child is not null and is not equal to the
                # last visited right child 
                # if this is the case then we can move the current to this pointer then also set the last
                # visited right child to this 
            # 5. 
                # else we process it by popping it off the stack 
                # whenever we process a node we set it to be the last visited
                # we will always process a right node right before its own node  or it wil lbe none 

    last_visited = None 
    curr = root  
    stack = []
    while stack or curr: 
        while curr:
            stack.append(curr)
            curr = curr.left 
        curr = stack[-1]
        if curr.right or curr.right != last_visited:
            curr = curr.right 
        else:
            last_visited = stack.pop() 
            print(curr.val, ",")
            curr = None # We want to start from the top of the stack 

# pre-order: root->left->right 
# def recursive_pre_order(): 
# def iterative_pre_order(): 

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