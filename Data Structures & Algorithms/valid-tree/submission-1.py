class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        pMap = {i: set() for i in range(n)}
        for p, c in edges:
            pMap[p].add(c)
            pMap[c].add(p)
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for c in pMap[i]:
                if c == prev:
                    continue
                if not dfs(c, i):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n