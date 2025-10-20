from collections import Counter

def deleteAndEarn(nums) -> int:

    # preprocess
    count = Counter(nums)

    # initialize dp states
    prev2 = prev1 = 0

    # Bottom-Up DP -> build up the max points accumulated after every operation
    for num in range(1, max(count)+1):
        curr = max(prev1, prev2 + (num * count.get(num, 0)) )
        prev2, prev1 = prev1, curr

    return prev1

    # Time:  O(n + m) -> m = max val in nums
    # Space: O(n)

nums = [3,4,2]
# nums = [3,1]
print(deleteAndEarn(nums))