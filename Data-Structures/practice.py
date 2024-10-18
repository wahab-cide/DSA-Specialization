class minHeap:
    def __init__(self):
        self.heap = []


    def insert(self, element):
        self.heap.append(element)
        self.heap._heapify_up(len(self.heap) - 1)

    def extractMax(self):
        if not self.heap:
            raise IndexError('Heap is empty')
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._heapify_up(0)
        return root
    


    def _heapify_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up[index]

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 + index + 1
        right_child_index = 2 * index + 2


        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[index]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[index]:
            smalest = right_child_index

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)



    

    def heapify(self, arr, n, i):
        largest = i
        left_index = 2 * 1 + 1
        right_index = 2 * 1 + 2



        if left_index < n and arr[left_index] > arr[largest]:
            largest = left_index

        if right_index < n and arr[right_index] > arr[largest]:
            largest = right_index

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)


    def heapsort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


# find Kth largest element

import heapq

def find_kth_largest(nums, k):
    min_heap = nums[:k]

    heapq.heapify(min_heap)


    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]



def merge_k_sorted_lists(lists):
    min_heap = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l[0], i, 0))
        