class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        result = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for n in graph[node]:
                dfs(n)


        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1

        return result