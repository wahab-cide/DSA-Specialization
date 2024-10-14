class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def pushFront(self, key): 
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node


    def popFront(self):
        if self.head is None:
            return None
        
        
        self.head = self.head.next
        return self.head.value
    
    def pushback(self, key):
        new_node = Node(key)

        if self.head is None:
            self.head = new_node


        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node = new_node




    def popBack(self):
      
        if self.head is None:
            return None

       
        if self.head.next is None:
            pop_node = self.head
            self.head = None
            return pop_node.value

        # Otherwise, find the second-to-last node
        second_last_node = self.head
        while second_last_node.next.next:  # Traverse until reaching the node before the last
            second_last_node = second_last_node.next

        # Remove the last node
        pop_node = second_last_node.next
        second_last_node.next = None
        return pop_node.value

        
    def pushBack(self, key):
        new_node = Node(key)

        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node



    def find(self, value):

        current = self.head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None
    
    def delete(self, data):

        if self.head is None:
            return

        if self.head.value == data:
            self.head = self.head.next
            return



        current = self.head
        while current.next:
            if current.value == data:
                current = current.next
                return
            current = current.next