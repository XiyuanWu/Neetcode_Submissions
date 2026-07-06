class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # pop [

                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number) * substr)

        return "".join(stack)