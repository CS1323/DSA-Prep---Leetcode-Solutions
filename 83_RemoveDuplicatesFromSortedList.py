# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    curr = head
    while curr and curr.next:

        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

    # Time:  O(n)
    # Space: O(1)

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node1.next = node2
node2.next = node3

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
head = deleteDuplicates(head=node1)
display(head)
