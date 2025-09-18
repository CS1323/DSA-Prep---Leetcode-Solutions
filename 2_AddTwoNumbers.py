# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    start = curr = ListNode()   # dummy node
    carry = 0

    while carry or l1 or l2:

        # add digits
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        # get val
        val = carry % 10
        carry = carry // 10

        # store val
        curr.next = ListNode(val)
        curr = curr.next

    return start.next

    # Time:  O(max(m,n))
    # Space: O(1) extra, O(max(m,n)) output size

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node_a = ListNode(5)
node_b = ListNode(6)
node_c = ListNode(4)

node1.next = node2
node2.next = node3
node_a.next = node_b
node_b.next = node_c

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
display(node_a)
head = addTwoNumbers(l1=node1, l2=node_a)
display(head)