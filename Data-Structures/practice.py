class minHeap:
    def __init__(self):
        self.heap = []


    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(element)

    def extractMin(self):
        if not self.heap:
            raise IndexError('Heap is empty')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        parent_index =  (index - 1) // 2


        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up[parent_index]

    def _heapify_down(self, index):
        smallest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2


        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down[smallest]