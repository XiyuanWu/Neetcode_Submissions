class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []

        l = 0
        for r in range(len(nums)):
            window.append(nums[r])

            # if not valid window length
            if (r - l + 1) > k:
                # remove previous value, add new value
                window.pop(0)
                l += 1

            # result will be max of this window
            if (r - l + 1) == k:
                result.append(max(window))
        
        return result