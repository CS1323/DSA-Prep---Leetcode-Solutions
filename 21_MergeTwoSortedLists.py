# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    temp_head = ListNode()   # temp node for reference
    curr = temp_head

    while list1 and list2:

        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    # add leftover nodes from larger linked list
    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return temp_head.next

    # Time:  O(n)
    # Space: O(1)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node_a = ListNode(1)
node_b = ListNode(3)
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
head = mergeTwoLists(list1=node1, list2=node_a)
display(head)