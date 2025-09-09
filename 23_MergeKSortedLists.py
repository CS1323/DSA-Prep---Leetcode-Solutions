import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):

    curr = start = ListNode() # dummy node
    heap = [] # min heap

    # build heap -> (root.value, list_index, root)
    #   idx used as tiebreaker
    for idx, root in enumerate(lists):
        if root:
            heapq.heappush(heap, (root.val, idx, root))
    
    while heap:
        _, idx, curr.next = heapq.heappop(heap)
        curr = curr.next
        # push next node from same list
        if curr.next: heapq.heappush(heap, (curr.next.val, idx, curr.next))

    return start.next

    # Time:  O(n log k)
    # Space: O(k)

def display(root):
    vals = []

    while root:
        vals.append(str(root.val))
        root = root.next

    print(" -> ".join(vals))

list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
merged_list = mergeKLists(lists)
display(merged_list)
