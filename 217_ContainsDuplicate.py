def containsDuplicate(nums) -> bool:
    nums_seen = set()

    for n in nums:
        
        if n in nums_seen:
            return True
        nums_seen.add(n)

    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))
