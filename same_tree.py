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

# test 1: same trees
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))  # expected: True

# test 2: different structure
p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

print(is_same_tree(p2, q2))  # expected: False

# test 3: different values
p3 = TreeNode(1)
p3.left = TreeNode(2)

q3 = TreeNode(1)
q3.left = TreeNode(3)

print(is_same_tree(p3, q3))  # expected: False