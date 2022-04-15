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
    currentSum = 0
    closestSum = float("inf")

    
    for i in range(len(arr) -2):
        leftP = i + 1
        rightP = len(arr) - 1
        currentSum = arr[i] + arr[leftP] + arr[rightP]
        # 

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
