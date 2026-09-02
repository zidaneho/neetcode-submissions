class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for token in tokens:
            if token == '+':
                t1 = stack.pop()
                t2 = stack.pop()
                print('adding',int(t2) + int(t1))
                stack.append(int(t2) + int(t1))
            elif token == '-':
                t1 = stack.pop()
                t2 = stack.pop()
                print('sub',int(t2) - int(t1))
                stack.append(int(t2) - int(t1))
            elif token == '*':
                t1 = stack.pop()
                t2 = stack.pop()
                print('mult',int(t2) *int(t1))
                stack.append(int(t2) * int(t1))
            elif token == '/':
                t1 = stack.pop()
                t2 = stack.pop()
               
                stack.append(math.trunc(int(t2) / int(t1)))
            else:
                stack.append(token)
            print('stack:',stack)
        
        return stack[0]