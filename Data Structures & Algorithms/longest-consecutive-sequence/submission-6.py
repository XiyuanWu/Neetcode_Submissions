class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        curr, longest = 1, 1

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1

        return longest