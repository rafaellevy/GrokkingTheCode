from turtle import left


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