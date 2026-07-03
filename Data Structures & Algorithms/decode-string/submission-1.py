class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in range(len(s)):
            if s[ch] != "]":
                stack.append(s[ch])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number) * substr)

        return "".join(stack)