from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):    # ← outside the class, no indentation
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        cur_level_res = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level_res.append(node.val)
        res.append(cur_level_res)
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order(root))
print(level_order(None))