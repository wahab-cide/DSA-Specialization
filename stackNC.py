# 1 valid parentheses

def isValid(s):

    stack = []
    matchingPairs = {']':'[', '}':'{', ')':'('}


    for c in s:
        if c in matchingPairs:
            if stack and stack[-1] == matchingPairs[c]:
                stack.pop()

            else:
                return False
            
        else:
            stack.append(c)

    return stack == []


# 2 design stack with push, pop, top, getMin

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        mini = min(val, self.minStack[-1] if self.minStack else val )
        self.minStack.append(mini)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

# 3 Evaluate Reverse Polish Notation

def eRPN(tokens):

    stack = []

    for c in tokens:

        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '*':
            stack.append(stack.pop() * stack.pop())

        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)

        elif c == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))

        else:
            stack.append(c)

    return stack[-1]


# 4 generate parenthese

def generateParenthese(n):

    stack = []
    res = []


    def backtrack(openN, closedN):

        if openN == closedN == n:
            res.append(''.join(stack))
            return
        
        if openN < n:
            stack.append('()')
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append('(')
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
            
# 5 daily temperatures

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res

# 6 car fleet
def carFleet(target, position, speed):

    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)

        if len(stack) >= 2 and stack[-1] >= stack[-2]:
            stack.pop()


    return len(stack)