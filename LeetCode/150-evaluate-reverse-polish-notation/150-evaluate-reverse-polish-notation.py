class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        def isinteger(num):
            try:
                int(num)
            except:
                return False
            else:
                return True
        
        
        stack = []
        
        for token in tokens:
            if not stack or isinteger(token):
                stack.append(token)
            else:
                number2, number1 = stack.pop(), stack.pop()
                # use int() to operate "/"
                temp = str(int(eval(number1 + token + number2)))
                stack.append(temp)
            # print(stack)
            
        return int(stack[-1])