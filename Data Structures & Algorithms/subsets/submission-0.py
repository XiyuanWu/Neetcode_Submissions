class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            new_subsets = []

            for subset in result:
                new_subsets.append(subset + [n])

            result += new_subsets

        return result