class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot_index = len(nums) // 2
        pivot = nums[pivot_index]
        left = []
        right = []

        for i in range(len(nums)):
            if i == pivot_index:
                continue
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        return self.sortArray(left) + [pivot] + self.sortArray(right)