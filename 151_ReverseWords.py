import operator
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        tokens = deque(tokens)
        result = deque()
        ops = {
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.truediv  # use operator.div for Python 2
                }

        while tokens:
            char = tokens.popleft()
            if char in "+-*/":
                num1 = int(result.pop())
                num2 = int(result.pop())
                calculated = ops[char](num2, num1)
                result.append(calculated)
            else:
                result.append(char)
            

        
        
        
        
        print(result)
        return int(result.pop())


        # Input: tokens = ["2","1","+","3","*"]
        '''
        - ["2","1","+","3","*"]
        while tokens is not none:   
        - 1. tokens.popleft() 
        - 2-1. if it is a number
                put in stack 
        - 2-2. elif it is a operator
                pop() two numbers from stack and do operate
                push() the result to the stack again





        '''
