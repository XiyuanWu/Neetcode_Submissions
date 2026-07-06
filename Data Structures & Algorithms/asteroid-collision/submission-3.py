class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if abs(a) == stack[-1]:
                    a = 0
                    stack.pop()
                elif abs(a) > stack[-1]:
                    stack.pop()
                else:
                    a = 0

            if a: 
                stack.append(a)
        
        return stack