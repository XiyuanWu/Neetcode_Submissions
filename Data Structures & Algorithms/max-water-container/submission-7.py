class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        maxA = 0

        for i in range(len(nums)):
            area = (r - l) * min(nums[l], nums[r])
            maxA = max(area, maxA)

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return maxA