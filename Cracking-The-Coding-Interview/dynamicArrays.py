#Data Structure Design(Dynamic Arrays)
# Design a dynamic array class that supports the following operations:
# 1. get(i): returns the element at index i
# 2. set(i, x): sets the element at index i to x
# 3. append(x): adds an element x to the end of the array
# 4. pop_back(): removes the last element from the array
# 5. resize(new_capacity): changes the capacity of the array to new_capacity
class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[i]
    
    def set(self, i, x):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.array[i] = x

    
    def append(self, x):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = x
        self.size += 1

    def resize(self,new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        self.size -= 1
        if self.size /self.capacity < 0.25 and self.capacity > 10:
            self.resize(self.capacity // 2)

    def pop_i(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        storedElement = self.array[i]
        for idx in range(i, self.size - 1):
            self.array[idx] = self.array[idx + 1]
        self.pop_back()
        return storedElement
    #use double ended queue(deque) if you find yourself 
    # constantly popping from both ends of an array(pg 384)