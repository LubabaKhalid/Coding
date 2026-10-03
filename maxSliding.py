#Brute Force logic
"""#nums = [1,3,-1,-3,5,3,6,7]
#k = 3
nums=[1]
k=1
i=0
l=[]
while k+i<=len(nums):
    l.append(max(nums[i:k+i]))
    i=i+1

print(l)"""

#Optimized Logic
import heapq

def maxSlidingWindow(nums, k):
    heap = []
    result = []

    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))

        if i >= k - 1:

            # Remove elements outside the window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            result.append(-heap[0][0])

    return result
nums = [1,3,-1,-3,5,3,6,7]
