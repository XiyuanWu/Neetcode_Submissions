class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                total = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            elif t == "-":
                total = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            elif t == "*":
                total = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(total)
            elif t == "/":
                total = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(total)
            else:
                stack.append(int(t))

        return sum(stack)