class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):        # ← no indentation, outside class
    slow = head
    fast = head
    while fast and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# test 1: cycle exists
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(has_cycle(node1))  # expected: True

# test 2: no cycle
node5 = ListNode(1)
node6 = ListNode(2)
node5.next = node6
print(has_cycle(node5))  # expected: False

# test 3: single node
node7 = ListNode(1)
print(has_cycle(node7))  # expected: False