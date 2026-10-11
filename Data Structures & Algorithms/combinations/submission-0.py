class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(start):
            if len(path) == k:
                result.append(path.copy())
                return

            for num in range(start, n+1):
                path.append(num)
                dfs(num + 1)
                path.pop()

        dfs(1)
        return result