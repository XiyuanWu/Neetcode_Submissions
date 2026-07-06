class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                result = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif t == "-":
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif t == "*":
                result = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif t == "/":
                result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[0]