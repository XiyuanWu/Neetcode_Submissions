class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        longest = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            while r - l + 1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest