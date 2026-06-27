class Solution:
    def trap(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        maxL, maxR = nums[left], nums[right]
        result = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, nums[left])
                result += maxL - nums[left]
            else:
                right -= 1
                maxR = max(maxR, nums[right])
                result += maxR - nums[right]

        return result