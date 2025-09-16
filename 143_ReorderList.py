# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    # base case
    if not head or not head.next:
        return

    # Find middle
    fast = slow = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    # Reverse 2nd half of the list
    prev = None
    curr = slow.next
    slow.next = None    # cut the list
    while (curr):
        temp1 = curr.next
        curr.next = prev
        prev = curr
        curr = temp1

    # Merge the 2
    first = head
    second = prev
    while (second):
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    return
    
    # Time:  O(n)
    # Space: O(1)

head = node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node5

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
reorderList(head)
display(head)
