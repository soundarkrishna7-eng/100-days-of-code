class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    # base case
    if root is None:
        return True
    # check boundaries
    if root.val <= min_val or root.val >= max_val:
        return False
    # recurse left (update max) and right (update min)
    return is_valid_bst(root.left, min_val, root.val) and \
           is_valid_bst(root.right, root.val, max_val)

# valid BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
print(is_valid_bst(root))  # True

# invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(6)  # 6 > 5, invalid
print(is_valid_bst(root2))  # False