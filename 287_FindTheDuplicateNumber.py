def findDuplicate(nums) -> int:

    # Slow & Fast Pointers (Floyd's Cycle Finding Algorithm)
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find start of cycle
    curr = nums[0]
    while curr != slow:
        curr = nums[curr]
        slow = nums[slow]

    return curr

    # Time:  O(n)
    # Space: O(1)

nums = [1,3,4,2,2]
print(findDuplicate(nums))