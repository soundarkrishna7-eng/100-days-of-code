class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    left = dummy
    right = dummy
    for i in range(n + 1):
        right = right.next
    while right is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

print_list(remove_nth_from_end(build_list([1,2,3,4,5]), 2))
print_list(remove_nth_from_end(build_list([1]), 1))
print_list(remove_nth_from_end(build_list([1,2]), 1))