class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# build linked list helper
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# print linked list helper
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# test
print_list(reverse_list(build_list([1,2,3,4,5])))  # [5,4,3,2,1]
print_list(reverse_list(build_list([1,2])))         # [2,1]
print_list(reverse_list(build_list([1])))           # [1]