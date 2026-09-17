class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_subtree(root, subRoot):
    if subRoot is None:
        return True
    if root is None:
        return False
    if is_same_tree(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

# build root tree:
#      3
#     / \
#    4   5
#   / \
#  1   2
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# build subRoot:
#    4
#   / \
#  1   2
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(is_subtree(root, subRoot))  # expected: True

# test 2: not a subtree
subRoot2 = TreeNode(4)
subRoot2.left = TreeNode(1)
subRoot2.right = TreeNode(3)  # different value

print(is_subtree(root, subRoot2))  # expected: False