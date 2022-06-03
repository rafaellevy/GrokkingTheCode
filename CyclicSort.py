# Cyclic Sort (easy)

'''
We are given an array containing n objects. 
Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. 
This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in 
O(n)
 and without using any extra space. For simplicity, lets assume we are passed an integer array 
 containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
'''

def cyclic_sort(nums):
    current = 1
    for i in range(len(nums)):
        nums[i] = current
        current +=1
    return nums

def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

# Cyclic Sort ( version 2 - better ) 

def cyclic_sort2(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if j != i + 1:
            swap(i,nums[i]-1,nums)
        else:
            i += 1
    return nums

def swap(x,y,arr):
    arr[x], arr[y] = arr[y], arr[x]


def main():
  print(cyclic_sort2([3, 1, 5, 4, 2]))
  print(cyclic_sort2([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort2([1, 5, 6, 4, 3, 2]))

main()

# Find the Missing Number (easy)

'''
We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''

def find_missing_number(nums):
    maximum = len(nums)+1

    auxArray = [None] * maximum

    for i in range(len(nums)):
        auxArray[nums[i]] = nums[i]
    
    for j in range(len(auxArray)):
        if auxArray[j] == None:
            return j



def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()


# Find the Missing Number (version 2 - Better)

def find_missing_number(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if j != i and j < len(nums):
            swap(i,j,nums)
        else:
            i += 1
        
    for i in range(0,len(nums)):
        if i != nums[i]:
            return i    
    return len(nums)
        
def swap(x,y,arr):
    arr[x], arr[y] = arr[y], arr[x]






def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()

# Find all Missing Numbers 

'''
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4

'''

def find_missing_numbers(nums):
    missingNumbers = []
    i = 0
    while i < len(nums):
        j = nums[i]
        if j != i + 1 and j != nums[j -1]:
            swap(i,j-1, nums)
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        else:
            missingNumbers.append(i+1)

    return missingNumbers

def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()


# Find the Duplicate Number 


'''
We are given an unsorted array containing n+1 numbers taken from the range 1 to n. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4


'''

def find_duplicate(nums):
    i = 0

    while True:
        if nums[i] == i + 1:
            i += 1
        if nums[i] != i + 1:
            value = nums[i]
            if nums[value - 1] != nums[i]:
                swap(i,value - 1,nums)
            else:
                return value

def swap(x,y,arr):
    arr[x], arr[y] = arr[y], arr[x]



print("find duplicate - for sure we have a duplicate")
def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()

# Find all Duplicate Numbers

'''
We are given an unsorted array containing n numbers taken from the range 1 to n.
 The array has some numbers appearing twice, 
 find all these duplicate numbers using constant space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]

'''

def find_all_duplicates(nums):
    i = 0
    output = []
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        elif nums[i] != i + 1:
            value = nums[i]
            if nums[value - 1] != nums[i]:
                swap(i,value - 1,nums)
            else:
                output.append(value)
                i += 1

    return output

def swap(x,y,arr):
    arr[x], arr[y] = arr[y], arr[x]

print(find_all_duplicates([3, 4, 4, 5, 5]))


# Find the Corrupt Pair (easy)#
'''
We are given an unsorted array containing n numbers taken from the range 1 to n. 
The array originally contained all the numbers from 1 to n, but due to a data error, 
one of the numbers got duplicated which also resulted in one number going missing. 
Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''
print("hello")
def find_corrupt_numbers(nums):
    output = []
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            value = nums[i]
            if nums[value - 1] == value:
                if value not in output:
                    output.append(value)
                i += 1
            else:
                swap(i,value - 1, nums)
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            output.append(i + 1)
            
    return output
        

    
def swap(x,y,arr):
    arr[x], arr[y] = arr[y], arr[x]


            
def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()