# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = fast = head
    
    # Slow & Fast Pointers (Floyd's Cycle Finding Algorithm)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

    # Time:  O(n)
    # Space: O(1)

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(hasCycle(head=node1))