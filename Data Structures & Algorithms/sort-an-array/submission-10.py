class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        pivot = nums[mid]
        
        left = []
        right = []

        for i in range(len(nums)):
            if i == mid:
                continue
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        return self.sortArray(left) + [pivot] + self.sortArray(right)