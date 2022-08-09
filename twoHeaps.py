
from heapq import *
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

# Maximize Capital (hard)


'''
Given a set of investment projects with their respective profits, 
we need to find the most profitable projects. 
We are given an initial capital and are allowed to invest only in a fixed number of projects.
Our goal is to choose projects that give us the maximum profit.
Write a function that returns the maximum total capital after selecting 
most profitable projects.
We can start an investment project only when we have the required capital. 
Once a project is selected, we can assume that its profit has become our capital.
'''


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    capitalMinHeap = []
    profitMaxHeap = []

    for i in range(len(capital)):
        heappush(capitalMinHeap, (capital[i], i))

    availableCapital = initialCapital

    for i in range(numberOfProjects):
        while capitalMinHeap and capitalMinHeap[0][0] <= availableCapital:
            project, ind = heappop(capitalMinHeap)
            heappush(profitMaxHeap, (-profits[ind]))

        if not profitMaxHeap:
            break

        availableCapital += -heappop(profitMaxHeap)

    return availableCapital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()

# Next Interval (hard)

'''
Given an array of intervals, find the next interval of each interval.
 In a list of intervals, for an interval i its next interval 
 j will have the smallest start greater than or equal to the end of i.

Write a function to return an array containing indices of the next interval of each input interval.
 If there is no next interval of a given interval, return -1. 
 It is given that none of the intervals have the same start point.

'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)

    # heaps for finding the maximum start and end
    maxStartHeap, maxEndHeap = [], []

    result = [0 for x in range(n)]
    for endIndex in range(n):
        heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
        heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))

    # go through all the intervals to find each interval's next interval
    for _ in range(n):
        # let's find the next interval of the interval which has the highest 'end'
        topEnd, endIndex = heappop(maxEndHeap)
        result[endIndex] = -1  # defaults to - 1
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            # find the the interval that has the closest 'start'
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex
            # put the interval back as it could be the next interval of other intervals
            heappush(maxStartHeap, (topStart, startIndex))

    return result


def main():

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
