from collections import heapq,List
#1 Kth Largest Element in a Stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    

#2 Last Stone Weight

def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)
    stones.append(0)
    return abs(stones[0]) 
        

#3 K Closest Points to Origin

def KClosest(points, k):

    minHeap = []

    for x, y in points:
        dist = (x**2 + y**2)
        minHeap.append([dist, x, y])
    heapq.heapify(minHeap)


    heapq.heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1

    return res


#4 kth Largest element


from collections import Counter, deque
#5 Task scheduler

def taskScheduler(tasks, n):

    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()

    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])

        if q and q[0][1] == time:
            heapq.heppush(maxHeap, q.popleft()[0])

    return time


#6 implement twitter


#7 Find Median From Data Stream
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and
            -1 * self.small[0] > self.large[0]):
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large)) 
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2