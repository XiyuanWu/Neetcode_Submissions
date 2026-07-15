class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        result = 0

        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.pop(0)
                l += 1

            window.append(s[r])
            result = max(result, len(window))

        return result