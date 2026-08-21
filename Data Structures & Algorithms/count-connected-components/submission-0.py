class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node):
            q = deque()
            q.append(node)
            visited.add(node)

            while q:
                val = q.popleft()
                for n in graph[val]:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)

        visited = set()
        result = 0

        for node in range(n):
            if node not in visited:
                bfs(node)
                result += 1

        return result