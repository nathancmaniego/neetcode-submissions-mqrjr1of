class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            for a, b in zip(first, second):
                if a != b: # rule only applies if differing letters in same pos
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
                else:
                    if len(first) > len(second):
                        return ""
        
        queue = deque(char for char in indegree if indegree[char] == 0)
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return "".join(order) if len(order) == len(indegree) else ""