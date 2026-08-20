class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next

# tests
print_list(merge_two_lists(build_list([1,2,4]), build_list([1,3,4])))  # [1,1,2,3,4,4]
print_list(merge_two_lists(build_list([]), build_list([])))             # []
print_list(merge_two_lists(build_list([]), build_list([0])))            # [0]