# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["*", "-", "+", "/"]:
                if i == '/':
                    res = int(stack[-2] / stack[-1]) if stack[-2] * stack[-1] >= 0 else -(-stack[-2] // stack[-1])
                elif i == '+':
                    res = stack[-1] + stack[-2]
                elif i == '-':
                    res = stack[-2] - stack[-1]
                elif i == '*':
                    res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]