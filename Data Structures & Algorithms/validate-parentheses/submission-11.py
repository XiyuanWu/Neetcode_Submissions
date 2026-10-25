class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}

        for s in string:
            if s in "([{":
                stack.append(s)
            else:
                if not stack: return False
                if stack[-1] != pair[s]: return False
                stack.pop()

        return not stack