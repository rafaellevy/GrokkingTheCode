
from heapq import heapify, heappop, heappush
from re import S
from statistics import median
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
