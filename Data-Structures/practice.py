class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None



    def pushFront(self, key):

        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def pushBack(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def popFront(self):
        if self.head is None:
            return None
        pop_node = self.head
        self.head = self.head.next
        return pop_node.data
    
    def popBack(self):
        if self.head is None:
            return None
        if self.head.next is None:
            pop_node = self.head
            self.head = None
            return pop_node.data
        
        last_two_node = self.head
        while last_two_node.next.next:
            last_two_node = last_two_node.next
        pop_node = last_two_node.next
        last_two_node.next = None
        return last_two_node.next.data
    

    def find(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next

        return None
    
    def delete(self, key):

        while self.head:
            if self.head.data == key:
                self.head = self.head.next
                self.head = None
            self.head = self.head.next

        return None
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node

        self.head =  prev

    def reverse_l(self):

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev 


    
    def merge_sorted_iterative(list1, list2):
        # Create a dummy node to act as the start of the merged list
        dummy = Node(0)
        # Use 'tail' to keep track of the end of the merged list
        tail = dummy

        # Traverse through both lists until one of them is exhausted
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining part of the non-exhausted list
        tail.next = list1 if list1 else list2

        # Return the merged list, skipping over the dummy node
        return dummy.next















    def merge_sorted(list1, list2):
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
    
    def find_cycle(self):

        if self.head is None or self.head.next is None:
            return False
        
        slow = fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    

    def remove_cycle(self):
        slow, fast = self.head, self.head
        cycle_exists = False


        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_exists = True
                break

        if not cycle_exists:
            return
        
        slow = self.head
        prev = None
        while slow != fast:
            slow = slow.next
            prev = fast
            fast = fast.next

        prev.next = None

    def find_middle(self):
        slow, fast = self.head, self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
    
    def length_L(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
            

        return count
    
    def remove_duplicates(self):

        current = self.head

        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next == runner.next.next
                else:
                    runner = runner.next

            current = current.next



