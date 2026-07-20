class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            while r - l + 1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result