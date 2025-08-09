def maxArea(height) -> int:
    left = 0
    right = len(height)-1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right-left)
        max_area = max(area, max_area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area

    # Time:  O(n)
    # Space: O(1)

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))