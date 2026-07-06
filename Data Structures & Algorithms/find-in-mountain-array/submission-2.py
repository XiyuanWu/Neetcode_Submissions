class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find peak index
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        peak = l

        # 2. Search left side: increasing
        l, r = 0, peak

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        # 3. Search right side: decreasing
        l, r = peak + 1, n - 1

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                # right side is decreasing
                # if val is too small, target is on the left
                r = mid - 1
            else:
                # val is too big, target is on the right
                l = mid + 1

        return -1