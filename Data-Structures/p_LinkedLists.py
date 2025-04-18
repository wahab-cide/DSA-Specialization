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
    
    def find(self, value):
            
            current = self.head

            while current:
                if current.value == value:
                    return current
                current = current.next

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
merge 2 sorted linked list
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


"""Problem: 
Given the head of a linked list, return the 
node where the cycle begins. If there is no cycle, 
return null.
"""

def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


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



"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy 
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10


            current.next = ListNode(total)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next    