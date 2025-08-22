# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    curr = head
    old_to_new = {}     # {original_node : copied_node}

    # copy linked list w/values
    while curr:
        copy = Node(curr.val)
        old_to_new[curr] = copy
        curr = curr.next

    curr = head

    # update next and random pointers
    while curr:
        copy = old_to_new[curr]
        copy.next = old_to_new.get(curr.next)
        copy.random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new.get(head)

    # Time:  O(n)
    # Space: O(n)

node1 = Node(7, None)
node2 = Node(13, 0)
node3 = Node(11, 4)
node4 = Node(10, 2)
node5 = Node(1, 0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

def display(head):
    curr = head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

display(node1)
head = copyRandomList(head=node1)
display(head)