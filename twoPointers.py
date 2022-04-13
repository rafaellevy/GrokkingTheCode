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
        

