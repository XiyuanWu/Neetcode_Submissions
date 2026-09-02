class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        memo = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in memo:
                return memo[i]

            # option 1: s[i] is extra
            result = 1 + dfs(i + 1)

            # option 2: try to match a dictionary word
            for j in range(i, len(s)):
                word = s[i:j + 1]

                if word in words:
                    result = min(result, dfs(j + 1))

            memo[i] = result
            return result

        return dfs(0)