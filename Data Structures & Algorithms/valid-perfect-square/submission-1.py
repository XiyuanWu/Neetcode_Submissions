class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        for i in range(46361):
            if i * i == num:
                return True
            elif i * i > num:
                return False

        return False