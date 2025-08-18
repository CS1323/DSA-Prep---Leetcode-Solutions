def calPoints(operations) -> int:
    record = []     # stack

    for i in range(len(operations)):
        
        # add score to stack
        if operations[i].isdigit() or (operations[i][0] == '-'):
            record.append(int(operations[i]))

        # add sum of previous two scores to stack
        elif operations[i] == '+':
            record.append(record[-1] + record[-2])
        
        # add new score that is double of the previous score
        elif operations[i] == 'D':
            record.append(record[-1] * 2)

        # remove previous score
        else:
            record.pop()

    return sum(record) # total score

    # Time:  O(n)
    # Space: O(n)

ops = ["5","2","C","D","+"]
print(calPoints(ops))