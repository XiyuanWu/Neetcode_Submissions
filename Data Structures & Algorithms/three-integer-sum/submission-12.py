class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return list(result)