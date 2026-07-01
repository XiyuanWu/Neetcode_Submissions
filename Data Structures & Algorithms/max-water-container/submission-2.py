class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxA = 0
        l, r = 0, len(nums) - 1

        while l < r:
            area = (r - l) * (min(nums[l], nums[r]))
            maxA = max(area, maxA)

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return maxA