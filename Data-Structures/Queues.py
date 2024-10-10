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


#Using doubly linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None




#Queue Using Doubly Linked List
"""
Queue:
enqueue: Adds an element to the rear.
dequeue: Removes and returns the front element.
peek: Returns the front element without removing it.
is_empty: Checks if the queue is empty.
__len__: Returns the size of the queue.

"""
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:  # Empty queue
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise IndexError("Dequeue from an empty queue")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def peek(self):
        if self.head is None:
            raise IndexError("Peek from an empty queue")
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
