def maximumSum(arr) -> int:

    n = len(arr)

    # dp_no_del[i]  = max subarray sum ending at i with NO deletion used
    # dp_with_del[i]= max subarray sum ending at i WITH one deletion used
    dp_no_del = [0] * n
    dp_with_del = [0] * n

    # base cases
    dp_no_del[0] = arr[0]
    dp_with_del[0] = float("-inf")  # cannot delete the only element and still end at index 0

    for i in range(1, n):

        # start new subarray, or extend previous subarray (Kadane's)
        dp_no_del[i] = max(arr[i], dp_no_del[i-1] + arr[i])         

        # delete curr element, or extend subarray w/earlier deletion
        dp_with_del[i] = max(dp_no_del[i-1], dp_with_del[i-1] + arr[i]) 

    # max subarray sum with or without deletion
    return max(max(dp_no_del), max(dp_with_del))

    # Time:  O(n)
    # Space: O(n)

arr = [2,-1,-1,10]
print(maximumSum(arr))