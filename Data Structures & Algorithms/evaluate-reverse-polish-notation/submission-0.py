class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                result = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(result)
            
            elif i == "-":
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)

            elif i == "*":
                result = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)

            elif i == "/":
                result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)

            else:   # number only
                stack.append(int(i))

        return stack[0]