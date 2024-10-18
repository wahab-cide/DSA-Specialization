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

# Heap Sort Algorithm

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example Usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)


# Find Kth Largest Element in an Array
import heapq

def find_kth_largest(nums, k):
    # Use a Min-Heap of size k
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print("Kth largest element is:", find_kth_largest(nums, k))  # Output: 5


# Merge K Sorted Lists
import heapq

def merge_k_sorted_lists(lists):
    min_heap = []

    # Put the first element of each list into the heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l[0], i, 0))  # (value, list_index, element_index)

    merged_list = []
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # If there's another element in the same list, add it to the heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list

# Example Usage
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Merged list is:", merge_k_sorted_lists(lists))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]


# Find Median from a Data Stream
import heapq

class MedianFinder:
    def __init__(self):
        # Max-Heap for the left half
        self.left_half = []
        # Min-Heap for the right half
        self.right_half = []

    def add_num(self, num):
        # Add to max-heap (left_half), so push negative value
        heapq.heappush(self.left_half, -num)

        # Ensure the max element of left_half is <= min element of right_half
        if (self.left_half and self.right_half and (-self.left_half[0]) > self.right_half[0]):
            val = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, val)

        # Balance the sizes of the two heaps
        if len(self.left_half) > len(self.right_half) + 1:
            val = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, val)
        if len(self.right_half) > len(self.left_half):
            val = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -val)

    def find_median(self):
        if len(self.left_half) > len(self.right_half):
            return -self.left_half[0]
        return (-self.left_half[0] + self.right_half[0]) / 2.0

# Example Usage
median_finder = MedianFinder()
median_finder.add_num(1)
median_finder.add_num(2)
print("Median is:", median_finder.find_median())  # Output: 1.5
median_finder.add_num(3)
print("Median is:", median_finder.find_median())  # Output: 2.0



n
































