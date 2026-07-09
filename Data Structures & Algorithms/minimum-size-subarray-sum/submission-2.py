class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        window_length = float("inf")

        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            # if valid window length
            while window_sum >= target:
                window_length = min(window_length, r - l + 1)
                window_sum -= nums[l]
                l += 1

        if window_length == float("inf"):
            return 0

        return window_length