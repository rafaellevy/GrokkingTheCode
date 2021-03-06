from collections import deque
from turtle import left, right
from xmlrpc.client import Boolean

def findTwoIndices(arr, target):
    leftP = 0
    rightP = len(arr) - 1
    output = [-1,-1] 

    while leftP < rightP:
        if arr[leftP] + arr[rightP] == target:
            return [leftP, rightP]
        elif arr[leftP] + arr[rightP] > target:
            rightP -= 1
        elif arr[leftP] + arr[rightP] < target:
            leftP += 1
    return output

print(findTwoIndices([1, 2, 3, 4, 6],6))
print(findTwoIndices([2, 5, 9, 11],11))

def removeDuplicates(arr):
    leftP = 0
    rightP = leftP + 1
    numberOfDuplicates = 0

    while rightP <= len(arr) - 1:
        if arr[leftP] == arr[rightP]:
            numberOfDuplicates += 1
        leftP += 1
        rightP += 1
    return len(arr) - numberOfDuplicates

print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
print(removeDuplicates([2, 2, 2, 11]))
        

def squaresOfAllTheNumbers(arr):
    leftP = 0
    rightP = len(arr) - 1
    output = []


    while leftP <= rightP:
        if arr[rightP]**2 >= arr[leftP]**2:
            output.append(arr[rightP]**2)
            rightP -= 1
        else:
            output.append(arr[leftP]**2)
            leftP += 1
    return list(reversed(output))

print(squaresOfAllTheNumbers([-2, -1, 0, 2, 3]))

print(squaresOfAllTheNumbers([-3, -1, 0, 1, 2]))



def tripletSumToZero(arr):
    arr.sort() 
    output = []

    
    for i in range(len(arr) -2):
        leftP = i + 1
        rightP = len(arr) - 1

        while leftP < rightP:

            if arr[i] + arr[leftP] + arr[rightP] == 0:
                output.append([arr[i],arr[leftP],arr[rightP]])
                leftP += 1
                rightP -= 1

            if arr[i] + arr[leftP] + arr[rightP] < 0:
                leftP += 1

            if arr[i] + arr[leftP] + arr[rightP] > 0:
                rightP -= 1

    return output

print(tripletSumToZero([-3, 0, 1, 2, -1, 1, -2]))
print(tripletSumToZero([-5, 2, -1, -2, 3]))


def tripletSumCloseToTarget(arr, target):
    arr.sort()
    ''' we don;t need to create closest sum in here 
    since line 101/103 will create the closest sum, always because any 
    difference will be smaller than infinity'''
    closestSum = float("inf")
    closestDifference = float("inf")

    for i in range(len(arr) -2):
        leftP = i + 1
        rightP = len(arr) - 1
        
        while leftP < rightP:
            currentSum = arr[i] + arr[leftP] + arr[rightP]
            currentDifference = abs(currentSum - target)
            if currentDifference < closestDifference:
                # created closestSum
                closestSum = currentSum
                closestDifference = currentDifference
            elif currentDifference == closestDifference:
                closestSum = min(currentSum, closestSum)

            if currentSum > target:
                rightP -= 1
            elif currentSum < target:
                leftP += 1
            else:
                leftP += 1
                rightP -= 1

    return closestSum

print("closest sum")
print(tripletSumCloseToTarget([-2, 0, 1, 2], 2))
print(tripletSumCloseToTarget([-3, -1, 1, 2], 1))
print(tripletSumCloseToTarget([1, 0, 1, 1], 100))

    

# triplets with sum smaller than target



def tripletSumSmallerThanTarget(arr, target):
    count = 0
    arr.sort()

    for i in range(len(arr) - 2):
        newTarget = target - arr[i]
        count += findPair(arr, newTarget, i )

    return count
           

def findPair(arr, target, idx):
    count = 0
    leftP = idx + 1
    rightP = len(arr) - 1

    while leftP < rightP:
        if arr[leftP] + arr[rightP] < target:
            count += rightP - leftP
            leftP += 1
        else:
            rightP -= 1
    
    return count

print("triplets smaller than target")
print(tripletSumSmallerThanTarget([-1, 0, 2, 3], 3))
print(tripletSumSmallerThanTarget([-1, 4, 2, 1, 3], 5))


def findProductSmallerThanTarget(arr, target):
    subArrays = []
    limit = len(arr) - 1

    for i in range(len(arr)):
        left = i + 1
        if arr[i] * 1 < target:
            subArrays.append([arr[i]])
        if i != limit and arr[i] * arr[left] < target:
            subArrays.append([arr[i],arr[left]])
    return subArrays
        
print("find product smaller than target")
print(findProductSmallerThanTarget([2, 5, 3, 10], 30))
print(findProductSmallerThanTarget([8, 2, 6, 5], 50))


# same problem using sliding window
def findProductSmallerThanTargetUsingSliding(arr, target):
    product = 1
    result = []
    windowStart = 0
    
    for windowEnd in range(len(arr)):
        product *= arr[windowEnd]
        while product >= target and windowStart < len(arr):
            product /= arr[windowStart]
            windowStart += 1

        tempList = deque()
        for i in range(windowEnd, windowStart - 1, - 1):
            tempList.appendleft(arr[i])
            result.append(list(tempList))

    return result

print("Using Sliding")
print(findProductSmallerThanTargetUsingSliding([2, 5, 3, 10], 30))
print(findProductSmallerThanTargetUsingSliding([8, 2, 6, 5], 50))


def dutchNationalFlag(arr):
    leftIdx = 0
    midIdx = 0
    rightIdx = len(arr) - 1

    while rightIdx >= midIdx:
        if arr[midIdx] == 0:
            swap(midIdx, leftIdx, arr)
            midIdx += 1
            leftIdx += 1
        elif arr[midIdx] == 2:
            swap(midIdx,rightIdx, arr)
            rightIdx -= 1
        else:
            midIdx += 1

    return arr

        
def swap(i, j, arr):
    arr[i],arr[j] = arr[j],arr[i]

print("dutch national flag")
print(dutchNationalFlag([1, 0, 2, 1, 0]))
print(dutchNationalFlag([2, 2, 0, 1, 2, 0]))


def quadrupleSumtoTarget(arr, target):
    arr.sort()
    output = set()
    for i in range(len(arr) - 4 + 1):
        p1 = i
        p2 = p1 + 1
        p3 = p2 + 1
        p4 = p3 + 1

        while True:
            sum = arr[p1] + arr[p2] + arr[p3] + arr[p4]
            print(sum)
            if sum > target:
                if p1 > 0:
                    p1 -= 1
                elif p2 > 1:
                    p2 -= 1
                elif p3 > 2:
                    p3 -= 1
                elif p4 > 3:
                    p4 -= 1
                else:
                    break
            elif sum < target:
                if p4 < len(arr) - 1:
                    p4 += 1
                elif p3 < len(arr) - 2:
                    p3 += 1
                elif p2 < len(arr) - 3:
                    p2 += 1
                elif p1 < len(arr) - 4:
                    p1 += 1
                else:
                    break
            elif sum == target:
                print(sum)
                output.add((arr[p1], arr[p2], arr[p3] , arr[p4]))
                break
    return list(output)

print("quadrupleSum")
print(quadrupleSumtoTarget([4, 1, 2, -1, 1, -3], 1))
print(quadrupleSumtoTarget([2, 0, -1, 1, -2, 2], 2))




def twoStringsBackspace(str1,str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    count = 0
    currentStr1 = ""
    currentStr2 = ""

    while p1 >= 0:
        if str1[p1] != "#":
            currentStr1 = str1[p1] + currentStr1
            p1 -= 1
            continue
        while str1[p1] == "#":
            count += 1
            p1 -= 1
        p1 -= count
        count = 0

    while p2 >= 0:
        if str2[p2] != "#":
            currentStr2 = str2[p2] + currentStr2
            p2 -= 1
            continue
        while str2[p2] == "#":
            count += 1
            p2 -= 1
        p2 -= count
        count = 0
    
    return currentStr1 == currentStr2


print("Backspace problem")
print(twoStringsBackspace("xy#z","xzz#"))
print(twoStringsBackspace("xy#z","xyz#"))
print(twoStringsBackspace("xp#","xyz##"))
print(twoStringsBackspace("xywrrmp","xywrrmu#p"))

def minimumWindowSort(arr):
    sortedArr = sorted(arr)
    uL = 0
    uR = len(arr) - 1
    sL = 0
    sR = len(arr) - 1

    while True:
        if arr[uL] != sortedArr[sL] and arr[uR] != sortedArr[sR]:
            return uR - uL + 1
        if arr[uL] == sortedArr[sL]:
            uL += 1
            sL += 1
        if arr[uR] == sortedArr[sR]:
            uR -= 1
            sR -= 1
        if uL == uR:
            return 0

print("minimumWindowSort")
print(minimumWindowSort([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimumWindowSort([1, 3, 2, 0, -1, 7, 10]))
print(minimumWindowSort([1, 2, 3]))
print(minimumWindowSort([3, 2, 1]))



def minimumWindowSort2(arr):
    low = 0
    high = len(arr) - 1

    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1
    
    if low == len(arr) - 1:
        return 0

    minimum = float("inf")
    maximum = float("-inf")

    for num in range(low, high + 1):
        minimum = min(minimum, arr[num])
        maximum = max(maximum,arr[num])

    while True:
        if low > 0 and minimum < arr[low - 1]:
            low -= 1
        elif low == 0:
            break
        else:
            break

    while True:
        if high < len(arr) - 1 and maximum > arr[high + 1]:
            high += 1
        elif high == len(arr) -1:
            break
        else:
            break

    return high - low + 1

print("minimumWindowSort 2")
print(minimumWindowSort2([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimumWindowSort2([1, 3, 2, 0, -1, 7, 10]))
print(minimumWindowSort2([1, 2, 3]))
print(minimumWindowSort2([3, 2, 1]))   
    
    
    


            
        
