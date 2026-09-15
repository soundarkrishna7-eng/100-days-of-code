class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def print_tree(root):
    if not root:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

# build tree:    4
#               / \
#              2   7
#             / \ / \
#            1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Before:", end=' ')
print_tree(root)
print()

invert_tree(root)

print("After:", end=' ')
print_tree(root)
print()
# expected after: 4 7 9 6 2 3 1