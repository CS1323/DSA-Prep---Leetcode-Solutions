# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    mid = head
    
    # Slow & Fast Pointers (Floyd's Cycle Finding Algorithm)
    while head and head.next:
        mid = mid.next
        head = head.next.next

    return mid

    # Time:  O(n)
    # Space: O(1)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
mid = middleNode(head=node1)
display(mid)