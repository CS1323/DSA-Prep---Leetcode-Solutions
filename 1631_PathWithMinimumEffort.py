from collections import defaultdict
import heapq

def minimumEffortPath(heights) -> int:
    ROWS, COLS = len(heights), len(heights[0])

    # Minimum effort required to reach each cell
    min_effort = [[float("inf")] * COLS for _ in range(ROWS)]
    min_effort[0][0] = 0

    # min-heap stores (effort, row, col)
    min_heap = [(0, 0, 0)] 

    # Dijkstra's algorithm
    while min_heap:

        curr_effort, r, c = heapq.heappop(min_heap)

        # return min_effort to destination
        if r == ROWS-1 and c == COLS-1:
            return curr_effort

        # skip outdated entries with higher effort
        if curr_effort > min_effort[r][c]:
            continue

        # explore valid neighbors
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            row, col = r+dr, c+dc

            if (row >= 0 and row < ROWS and 
                col >= 0 and col < COLS):

                edge_weight = abs(heights[r][c] - heights[row][col])
                new_effort = max(curr_effort, edge_weight)  # cost of path

                # update if a path with lower max effort is found
                if new_effort < min_effort[row][col]:
                    min_effort[row][col] = new_effort
                    heapq.heappush(min_heap, (new_effort, row, col))

    # Time:  O( (m*n) * log(m*n) )
    # Space: O(m*n)

heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPath(heights))