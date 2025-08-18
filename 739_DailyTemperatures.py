def dailyTemperatures(temperatures):
    stk = []
    n = len(temperatures)
    result = [0] * n

    for i in range(n):

        # update days to wait (result) while current temp is larger than the top of the stack's temp
        while stk and temperatures[i] > temperatures[stk[-1]]:
            temp_idx = stk.pop()
            result[temp_idx] = i - temp_idx
                    
        stk.append(i)

    return result

    # Time:  O(n)
    # Space: O(n)

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))