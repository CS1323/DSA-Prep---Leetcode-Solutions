from collections import defaultdict

def canFinish(numCourses, prerequisites) -> bool:

    adj_list = defaultdict(list)
    for u,v in prerequisites:
        adj_list[u].append(v)

    visit = [0] * numCourses    # visit states: 0=not_visited, 1=visiting, 2=visited

    def detectCycle(node):
        # found cycle
        if visit[node] == 1:
            return True
        # already visited -> no cycle
        if visit[node] == 2:
            return False
        
        visit[node] = 1     # mark as visiting

        for nei in adj_list[node]:
            if detectCycle(nei):
                return True

        visit[node] = 2     # mark as visiting     
        return False        # no cycle found

    for course in range(numCourses):
        if detectCycle(course):
            return False

    # no cycles
    return True

    # Time:  O(v+e)
    # Space: O(v+e)

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))