class KthLargest:

    def __init__(self, k, nums):
        self.heap = nums
        heapq.heapify(self.heap)
        self.num = k

    def add(self, val):
        heapq.heappush(self.heap, val)
        for i in range(len(self.heap)-self.num):
            heapq.heappop(self.heap)
        return self.heap[0]
