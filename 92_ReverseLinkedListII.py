# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    # prev_left = node before reversal
    prev = start = prev_left = ListNode(val=0, next=head)
    curr = head

    for i in range(1, right+1):
        temp = curr.next

        # point to node before reversal
        if i <= left:
            prev_left = prev
        # reverse pointer
        else:
            curr.next = prev
        
        prev = curr
        curr = temp

    # update connections to the rest of the (non-reversed) list
    if head.next:
        prev_left.next.next = curr
        prev_left.next = prev

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
left = 2
right = 4
head = reverseBetween(head=node1, left=left, right=right)
display(head)
