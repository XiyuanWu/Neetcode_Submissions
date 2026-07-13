class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        window = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(string)):
            window[string[r]] += 1

            while r - l + 1 - max(window.values()) > k:
                window[string[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
