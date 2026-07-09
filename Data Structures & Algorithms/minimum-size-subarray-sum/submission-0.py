class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = []
        window_length = float("inf")

        l = 0
        for r in range(len(nums)):
            window.append(nums[r])

            # if valid window length
            while sum(window) >= target:
                window_length = min(window_length, len(window))
                window.pop(0)
                l += 1

        if window_length == float("inf"):
            return 0

        return window_length