def compareVersion(version1: str, version2: str) -> int:

    v1_revisions = version1.split('.')
    v2_revisions = version2.split('.')

    # pad zeroes
    if len(v1_revisions) < len(v2_revisions):
        v1_revisions.extend('0' * (len(v2_revisions)-len(v1_revisions)))
    else:
        v2_revisions.extend('0' * (len(v1_revisions)-len(v2_revisions)))
    
    for i in range(len(v1_revisions)):

        v1_rev = int(v1_revisions[i])
        v2_rev = int(v2_revisions[i])

        # compare revisions
        if v1_rev < v2_rev:
            return -1
        if v1_rev > v2_rev:
            return 1
        
    return 0    # no difference
        
    # Time:  O(n)
    # Space: O(n)

version1 = "1.2"
version2 = "1.10"
version1 = "1.01"
version2 = "1.001"
print(compareVersion(version1, version2))