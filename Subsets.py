from collections import deque
# Subsets

'''
Given a set with distinct elements, find all of its distinct subsets.
'''


from itertools import permutations
from operator import length_hint


def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current
        # number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and
            # insert the current element to it
            set1 = list(subsets[i])
            set1.append(currentNumber)
            subsets.append(set1)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


# Subsets With Duplicates


'''
Given a set of numbers that might contain duplicates, 
find all of its distinct subsets.
'''


def find_subsets(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step
        if i > 0 and nums[i] == nums[i - 1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            # create a new subset from the existing subset and add the current element to it
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

# Permutations

'''
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set
'''


def find_permutations(nums):
    result = []
    # TODO: Write your code here
    length_nums = len(nums)
    permutations = deque()
    permutations.append([])

    for currentNumber in nums:
        n = len(permutations)

        for _ in range(n):
            oldPermutation = permutations.popleft()

            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == length_nums:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


main()


# Permutations (recursively)

def find_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            generate_permutations_recursive(
                nums, index + 1, newPermutation, result)


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


main()
