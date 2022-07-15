# Problem Statement

'''
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level 
from left to right in separate sub-arrays.
'''

from collections import deque
import queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    myQueue = [root]
    result = []

    while myQueue:
        levelArray = []
        level_length = len(myQueue)

        for _ in range(level_length):
            curNode = myQueue.pop(0)
            levelArray.append(curNode.val)
            if curNode.left:
                myQueue.append(curNode.left)
            if curNode.right:
                myQueue.append(curNode.right)

        result.append(levelArray)

    

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
