import heapq

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime, endTime) -> int:
        n = len(startTime)
        
        maxHeap = []
        heapq.heapify(maxHeap)

        heapq.heappush(maxHeap, -startTime[0])
        heapq.heappush(maxHeap, -(eventTime-endTime[-1]))

        for i in range(n-1):
            heapq.heappush(maxHeap, -(startTime[i + 1]-endTime[i]))

        print(maxHeap)

        if not maxHeap:
            return 0

        res = -heapq.heappop(maxHeap)

        while k:
            res += -heapq.heappop(maxHeap)
            k -= 1

        return res
            
            



solution = Solution()

eventTime = 21
k = 1
startTime = [7,10,16]
endTime =   [10, 14, 18]

print("res:", solution.maxFreeTime(eventTime, k, startTime, endTime))

