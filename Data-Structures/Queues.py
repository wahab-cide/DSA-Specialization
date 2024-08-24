"""
Queues: (First-In-First-Out)
When the order of processing matters 
and tasks need to be managed in the order they were received.

Appliactions:

1. Task Scheduling
2. Breadth-First-Search(level order processing)
3. Buffer Management

Array-Based Queue Implementation:
-init: Use a fixed-size array, with two pointers: 
front (points to the first element) and 
rear (points to the last element).

-enqueue: Add elements to the rear and 
move the rear pointer forward.

-dequeue: Remove elements from the front and 
move the front pointer forward.

-when array ends, rear pointer wrps around to 
the start of array

"""

class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, item):
        if self.is_full:
            raise Exception("Queue is full")
        if self.front == -1:
            self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item
