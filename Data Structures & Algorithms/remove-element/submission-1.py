class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x!= val]  # Give me x, for each x in nums, if x is not val.
        return len(nums)