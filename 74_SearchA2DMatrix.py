def searchMatrix(matrix, target):
    ######## find row ########
    left = 0
    right = len(matrix)-1

    # binary search
    while left <= right:
        row = left + ((right - left) // 2)

        if matrix[row][-1] < target:
            left = row + 1
        elif matrix[row][0] > target:
            right = row - 1
        else:
            break

    ######## find target value ########
    left = 0
    right = len(matrix[0])-1

    # binary search
    while left <= right:
        mid = left + ((right - left) // 2)

        if matrix[row][mid] < target:
            left = mid + 1
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            return True

    return False

    # Time:  O( log(m*n) ) -> m=rows, n=cols
    # Space: O(1)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))
