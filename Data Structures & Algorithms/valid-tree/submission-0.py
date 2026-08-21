class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:

                # don't go immediately back to where we came from
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        # check cycle starting from node 0
        if not dfs(0, -1):
            return False

        # also must be connected
        return len(visited) == n