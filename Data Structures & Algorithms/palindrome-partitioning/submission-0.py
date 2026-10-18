class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def dfs(start):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if part == part[::-1]:
                    path.append(part)
                    dfs(end)
                    path.pop()

        dfs(0)
        return result