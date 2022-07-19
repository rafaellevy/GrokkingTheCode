# Problem Statement

'''
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level 
from left to right in separate sub-arrays.
'''

from collections import deque
from operator import length_hint
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

'''
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the 
same manner for the following levels.
'''

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

# Level Averages in a Binary Tree
'''
Given a binary tree, 
populate an array to represent the averages of all of its levels.
'''

def find_level_averages(root):
    result = []
    queue = [root]
    
    
    while queue:
        length = len(queue)
        levelValue = 0

        for _ in range(length):
            node = queue.pop(0)
            levelValue += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


        result.append(levelValue/length)
    
    return result 
            

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()


# Minimum Depth of a Binary Tree

'''
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along 
the shortest path from the root node to the nearest leaf node.
'''

def find_minimum_depth(root):
    # TODO: Write your code here
    queue = [root]
    minDepth = 0

    while True:
        length = len(queue)
        minDepth += 1

        for _ in range(length):
            node = queue.pop(0)
            if not node.left and not node.right:
                return minDepth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                

    







    return -1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
