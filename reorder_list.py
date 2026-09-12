class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    # step 1: find middle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    second = slow.next
    slow.next = None
    prev = None
    current = second
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second = prev

    # step 3: merge
    first = head
    while second:
        next1 = first.next
        next2 = second.next
        first.next = second
        second.next = next1
        first = next1
        second = next2

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

head1 = build_list([1,2,3,4])
reorder_list(head1)
print_list(head1)  # expected: [1,4,2,3]

head2 = build_list([1,2,3,4,5])
reorder_list(head2)
print_list(head2)  # expected: [1,5,2,4,3]