class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        amt = 0
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        q = deque([])
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            q.append(i)
            while q:   
                node = q.popleft()
                for nei in graph[node]:
                    q.append(nei)
                visited.add(node)
                graph[node] = []
            amt += 1
        return amt
            