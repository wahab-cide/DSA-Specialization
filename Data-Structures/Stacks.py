"""
Stack implemented with an array or linked lists.
The last element added to the 
stack will be the first one to be removed.(LIFO)

Two main operations:
1. Push
2. Pop

Stack implementation:
1. Arrays: Fixed-size implementation 
where the stack has a maximum capacity.
(Con: Fixed size, leading to potential 
overflow if the stack exceeds its capacity.)

2. Linked Lists: Dynamic-size implementation 
where the stack can grow or shrink as needed. 
(Cons: xtra memory for pointers)
"""

class StackArray:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            raise Exception("Stack Overflow")
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
        else:
            raise Exception("Stack Underflow")
        
    def peek(self, capacity): #Return top element without removing it.
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return 'Stack sempty'
        else:
            self.head = self.head.next
            return self.head.data
        
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise Exception("Stack is empty")


#Popular Problems        
""""
Problem 1: Given a string containing just 
the characters '(', ')', '{', '}', '[', and ']', 
determine if the input string is valid. 
The string is considered valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Solution:

Idea: Push each opening bracket onto the stack 
and pop the stack when a closing bracket is encountered. 
If at the end of the traversal the stack is empty, 
the parentheses are balanced.
"""

#Algorithm:
"""
-Initialize a stack to keep track of opening brackets.

-Iterate through each character in the string:
--If the character is an opening bracket ('(', '{', '['), 
push it onto the stack.
--If the character is a closing bracket (')', '}', ']'):
---Check if the stack is empty. If it is, return False because 
there's no corresponding opening bracket.
---Pop the top of the stack and check if the popped bracket 
matches the closing bracket. If it doesn't match, return False.

-After iterating through the string, check if the stack is empty:
--If the stack is empty, all the opening brackets had matching closing 
brackets in the correct order, so return True.
--If the stack is not empty, return False because there are unmatched opening brackets.


"""

def IsBalanced(str):
    stack = []

    #dictionary to hold matching pairs
    matchingPairs = {')': '(', '}': '{', ']': '['}

    for char in str:
        if char in matchingPairs.values():
            stack.append(char)

        elif char in matchingPairs.keys():
            if stack.is_empty:
                return False
            
            elif stack.pop() != char:
                return False
            else:
                continue
    
    return stack == []  #if balanced, stack is empty, True
    