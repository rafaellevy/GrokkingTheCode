
from heapq import heapify, heappop, heappush
from re import S
from statistics import median
from unittest import result
# Find the Median of a Number Stream
'''
Design a class to calculate the median of a number stream.
 The class should have the following two methods:

- insertNum(int num): stores the number in the class
- findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, 
the median will be the average of the middle two numbers.

'''


class MedianOfAStream:
    def __init__(self) -> None:
        # minheap should contain the second half of the array ( larger half)
        self.minHeap = []
        self.maxHeap = []

    def insert_num(self, num):

        # TODO: Write your code here
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heappush(self.minHeap, num)
        elif num > self.minHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            # rebalancing
            topMinHeap = heappop(self.minHeap)
            # max heap is a min heap ( add - sign)
            heappush(self.maxHeap, -topMinHeap)

        elif len(self.maxHeap) > len(self.minHeap):
            topMaxHeap = heappop(self.maxHeap)
            # max heap is a min heap ( add - sign to go back to positive)
            heappush(self.minHeap, -topMaxHeap)

    def find_median(self):

        print(self.minHeap)
        print(self.maxHeap)
        # TODO: Write your code here
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            result = (self.minHeap[0] + -self.maxHeap[0]) / 2

            return result


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()

# Sliding Window Median

"""
    Given an array of numbers and a number k, 
    find the median of all the k sized sub-arrays 
    (or windows) of the array.
    """


class SlidingWindowMedian:
    def __init__(self) -> None:
        # minheap should contain the second half of the array ( larger half)
        self.minHeap = []
        self.maxHeap = []
        self.result = []

    def find_sliding_window_median(self, nums, k):
        # TODO: Write your code here
        windowStart = 0
        windowEnd = 0

        # add first number to heap
        self.insert_num(nums[windowEnd])

        for i in range(len(nums)):
            if windowEnd - windowStart + 1 == k:
                self.result.append(self.find_median(
                    nums[windowStart:windowEnd + 1]))
                # TODO: remove the start number from min or max heap
                self.remove(windowStart, nums)
                windowStart += 1

            windowEnd += 1
            if windowEnd < len(nums):
                self.insert_num(nums[windowEnd])

        return self.result

    # we are removing the number that will be out of the window once we slide the window to the right
    def remove(self, idx, arr):
        # num to remove
        num = arr[idx]
        # find which heap it must be.
        if num >= self.minHeap[0]:
            # find the index where num is
            heap_idx = self.minHeap.index(num)
            # swap it with the last index, pop the last index off
            self.minHeap[heap_idx] = self.minHeap[-1]
            self.minHeap.pop()
            # heapify the minHeap
            heapify(self.minHeap)
        else:
            heap_idx = self.maxHeap.index(-num)
            self.maxHeap[heap_idx] = self.maxHeap[-1]
            self.maxHeap.pop()
            heapify(self.maxHeap)

         # rebalance heap
        self.rebalance_Heap()

    def rebalance_Heap(self):
        # Since we removed one from the max or min heap, we may need to rebalance the heaps
        if len(self.minHeap) > len(self.maxHeap) + 1:
            # rebalancing
            topMinHeap = heappop(self.minHeap)
            # max heap is a min heap ( add - sign)
            heappush(self.maxHeap, -topMinHeap)

        elif len(self.maxHeap) > len(self.minHeap):
            topMaxHeap = heappop(self.maxHeap)
            # max heap is a min heap ( add - sign to go back to positive)
            heappush(self.minHeap, -topMaxHeap)

    def insert_num(self, num):

        # TODO: Write your code here
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heappush(self.minHeap, num)
        elif num > self.minHeap[0]:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)

        # rebalance heap
        self.rebalance_Heap()

    def find_median(self, window):

        # TODO: Write your code here
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            resultMedian = (self.minHeap[0] + -self.maxHeap[0]) / 2

            return resultMedian


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
