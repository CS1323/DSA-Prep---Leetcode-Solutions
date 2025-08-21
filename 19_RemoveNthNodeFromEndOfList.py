# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    start = ahead = behind = ListNode()
    start.next = head
    
    for _ in range(n+1):
        ahead = ahead.next

    while ahead:
        ahead = ahead.next
        behind = behind.next

    behind.next = behind.next.next

    return start.next

    # Time:  O(n)
    # Space: O(1)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
head = removeNthFromEnd(head=node1, n=2)
display(head)