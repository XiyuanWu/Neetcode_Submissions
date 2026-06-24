class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()

        current, longest = 1, 1

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
                longest = max(current, longest)
            else:
                current = 1

        return longest