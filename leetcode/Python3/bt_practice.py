from utils.binary_tree import TreeNode, BinaryTree

nodes = [65,20,70,10,22,68,75]
root = BinaryTree.build_tree(nodes)

"""  
    In-Order BT DFS Traversal  
    Left->Current->Right
"""
def in_order(root: TreeNode, state: list) -> list:
    if not root:
        return
    if root.left:
        in_order(root.left, state)
    state.append(root.val)
    if root.right:
        in_order(root.right, state)

    return state
    
print(f"Inorder: {in_order(root, [])}")

"""  
    Pre-Order BT DFS Traversal  
    Current->Left->Right
"""
def pre_order(root: TreeNode, state: list) -> list:
    if root:
        state.append(root.val)
        if root.left:
            pre_order(root.left, state)
        if root.right:
            pre_order(root.right, state)
    
    return state

print(f"Pre-Order: {pre_order(root, [])}")

"""  
    Post-Order BT DFS Traversal  
    Left->Right->Current
"""
def post_order(root: TreeNode, state: list) -> list:
    if root:

        if root.left:
            post_order(root.left, state)
        if root.right:
            post_order(root.right, state)
        state.append(root.val)
            
    return state

print(f"Post-Order: {post_order(root, [])}")