# Problem Statement

'''
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level 
from left to right in separate sub-arrays.
'''

from collections import deque
import queue
from turtle import left


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


# Reverse Level Order Traversal

'''
Problem Statement#
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., 
the lowest level comes first. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
'''


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

    

    return result[::-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))

main()

# Zigzag Traversal

def traverse(root):
  result = []
  queue = [root]
  isLeft = True


  while queue:
    currentLevel = []
    length = len(queue)

    for _ in range(length):
      node = queue.pop(0)
      currentLevel.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    if isLeft == False:
        result.append(currentLevel[::-1])
    else:
        result.append(currentLevel)
    # flip bool
    isLeft =  not isLeft
        
  
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()