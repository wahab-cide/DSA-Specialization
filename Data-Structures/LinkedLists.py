class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, key):   #O(1)
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def popFront(self): #O(1)
        if self.head is None:
            return None
        
        self.head = self.head.next
        return self.head.data
    
      
    def pushBack(self, key): #O(N)
        new_node = Node(key)

        if self.head is None:
            self.head = new_node
            return
        

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def popBack(self):  #O(N)
        if self.head is None:
            return None
        if self.head.next is None:
            pop_node = self.head
            self.head = None
            return pop_node.data
        
        second_last_node = self.head
        while second_last_node.next:
            second_last_node = second_last_node.next
        second_last_node= None
        return  second_last_node.data
    

    def find(self, key):    #O(N) NOT CORRECT
        if self.head is None:
            return None
        
        if self.head.data == key:
            return self.head.data
        
        while self.head != key:
            self.head = self.head.next
        return self.head.next.data


    def find_2(self, key): #O(N)
        while self.head:
            if self.head == key:
                return self.head.data
            self.head = self.head.next
        return None
    
    def delete(self, key):  #O(N)
        while self.head:
            if self.head.data == key:
                self.head = self.head.next
                self.head = None
            self.head = self.head.next
        return None


#Reverse linked list
"""
Idea: head node becomes the last node,
 and the last node becomes the head

"""
def reverse(self):
    prev_node = None
    current_node = self.head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    self.head = prev_node


#Merge two sorted linked lists
"""
merge 2 sorted linsked list
Base case: if one list is empty, 
return the other lsit.

Else, recursively merge the two lists.
Compare the data of the heads of both lists. 
Whichever node has the smaller value becomes
the head of the merged list. Recursively
repeat this process for the rest of the lists.

Algorithm:
Recursively compare the heads of both lists.
Set the next of the smaller node to the result
of merging the rest of the lists.
Continue until one list is exhausted.

"""
def merge_sorted(list1, list2):

    if not list1:
        return list2
    if not list2:
        return list1
        
    if list1.data < list2.data:
        result = list1
        result.next = merge_sorted(list1.next, list2)

    else:
        result = list2
        result.next = merge_sorted(list1, list2.next)

    return result

#Remove cycles
"""

Algorithm:
Floyd's Cycle-Finding Algorithm
-Use two pointers (slow and fast) to detect the cycle.
-After detecting, find the cycle's starting point.
-Remove the cycle by setting the last node's next to None.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        if self.head is None or self.head.next is None:
            return False
        
        slow = fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.remove_cycle(slow)
                return True
        return False
                                                                    
    def remove_cycle(self, loop_node):
        ptr1 = self.head

        while True:
            ptr2 = loop_node

            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next

            if ptr2 == ptr1:
                break
            ptr1 = ptr1.next

        ptr2.next = None



#Find middle element
"""
Two pointer: slow, fast = self.head
slow.next, fast.next.next

When fast reaches the end of the list,
slow will be at the middle. return slow.data

"""
def find_middle(self):
    slow = fast = self.head

    while fast and fast.next:
        slow = slow.next
        fast =fast.next.next

    return slow.data


#Remove duplicates

"""
Traversal algorithm.
- Start from the head of the list and 
traverse through the list.
-For each node, compare its data with 
the data of the following nodes 
(using a runner pointer)
-if a duplicate is found, skip the duplicate 
node by changing the next pointer of the previous
node to the node after the duplicate.

Hint: Use a nested loop: an outer loop to 
pick nodes one by one, and an inner loop to 
check for duplicates.
"""

def remove_duplicates(self):

    current = self.head

    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

