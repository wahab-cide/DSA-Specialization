class MinHeap:
    def __init__(self):
        self.heap = []

    # Insert a new element into the heap
    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    # Remove and return the smallest element (root) from the heap
    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    # Heapify up (used after insertion)
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap if the current element is smaller than its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    # Heapify down (used after extraction)
    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Check if the left child is smaller
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        # Check if the right child is smaller
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        # If the smallest element is not the current element, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    # Return the smallest element without removing it
    def get_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]





#problems

