class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack:
                    if stack[-1] != pair[ch]:
                        return False

                    stack.pop()

                else:
                    return False

        return not stack