class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        window_len = float("inf")

        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                window_len = min(window_len, r - l + 1)
                window_sum -= nums[l]
                l += 1

        if window_len == float("inf"):
            return 0

        return window_len