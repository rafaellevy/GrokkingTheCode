# Binary Tree Path Sum

import math
from re import S


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()


# All Paths for a Sum
'''
Given a binary tree and a number S,
find all paths from root-to-leaf such that the
sum of all the node values of each path equals S.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []

    find_paths_helper(root, sum, [], allPaths)

    return allPaths


def find_paths_helper(root, sum, currentPath, allPaths):
    if root == None:
        return

    currentPath.append(root.val)

    if root.val == sum and root.left == None and root.right == None:
        allPaths.append(list(currentPath))
    else:
        find_paths_helper(root.left, sum - root.val, currentPath, allPaths)
        find_paths_helper(root.right, sum - root.val, currentPath, allPaths)

    # remove last node visited from the call stack
    currentPath.pop()


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()


# Sum of Path Numbers

'''
Given a binary tree where each node can only have a digit (0-9) value,
each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here
    totalSum = 0

    return find_sum_of_path_numbers_helper(root, "", totalSum)


def find_sum_of_path_numbers_helper(root, currentNumber, sum):
    if root == None:
        return 0

    currentNumber += str(root.val)

    if root.left == None and root.right == None:
        sum += int(currentNumber)
        return sum

    # not necessary to delete the last letter from the string
    # currentNumber = currentNumber[:len(currentNumber)-1]

    return find_sum_of_path_numbers_helper(root.left, currentNumber, sum) + find_sum_of_path_numbers_helper(root.right, currentNumber, sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()

# Path With Given Sequence

"""
Given a binary tree and a number sequence,
find if the sequence is present as a root-to-leaf path in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):

    return find_path_helper(root, "", sequence)


def find_path_helper(root, currentString, sequence):
    if root == None:
        return False

    currentString += str(root.val)

    if root.left == None and root.right == None:
        currentSequence = list(currentString)
        currentSequence = [int(x) for x in currentSequence]
        print(currentSequence)
        return currentSequence == sequence

    return find_path_helper(root.left, currentString, sequence) or find_path_helper(root.right, currentString, sequence)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


# Count Paths for a Sum


'''
Given a binary tree and a number S,
find all paths in the tree such that the sum of all the node values of each path equals S.
Please note that the paths can start or end at any node but all paths must follow direction
from parent to child (top to bottom).

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0

    # add the current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count.
        if pathSum == S:
            pathCount += 1

    # traverse the left sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    # traverse the right sub-tree
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    # 11
    print("Tree has paths: " + str(count_paths(root, 23)))


main()


# Tree Diameter

"""
Given a binary tree,
find the length of its diameter.
The diameter of a tree is the number of nodes on the longest path
between any two leaf nodes.
The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least
two leaf nodes in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        # if the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        if leftTreeHeight != 0 and rightTreeHeight != 0:

            # diameter at the current node will be equal to the height of left subtree +
            # the height of right sub-trees + '1' for the current node
            diameter = leftTreeHeight + rightTreeHeight + 1

        # update the global tree diameter
            self.treeDiameter = max(self.treeDiameter, diameter)

    # height of the current node will be equal to the maximum of the heights of
    # left or right subtrees plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:

    def find_maximum_path_sum(self, root):
        self.globalMaximumSum = -math.inf
        self.find_maximum_path_sum_recursive(root)
        return self.globalMaximumSum

    def find_maximum_path_sum_recursive(self, currentNode):
        if currentNode is None:
            return 0

        maxPathSumFromLeft = self.find_maximum_path_sum_recursive(
            currentNode.left)
        maxPathSumFromRight = self.find_maximum_path_sum_recursive(
            currentNode.right)

        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
        maxPathSumFromRight = max(maxPathSumFromRight, 0)

        # maximum path sum at the current node will be equal to the sum from the left subtree +
        # the sum from right subtree + val of current node
        localMaximumSum = maxPathSumFromLeft + maxPathSumFromRight + currentNode.val

        # update the global maximum sum
        self.globalMaximumSum = max(self.globalMaximumSum, localMaximumSum)

        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(maxPathSumFromLeft, maxPathSumFromRight) + currentNode.val


def main():
    maximumPathSum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()

# comment added
