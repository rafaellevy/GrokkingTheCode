from __future__ import print_function
from operator import le, length_hint
import queue


# Problem Statement

'''
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level 
from left to right in separate sub-arrays.
'''


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


# Level Order Successor

'''
Given a binary tree and a node, 
find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after 
the given node in the level order traversal.
'''

def find_successor(root, key):
    # TODO: Write your code here
    queue = [root]
    result = []
    ind = None

    while queue:
        length = len(queue)
        for _ in range(length):
            node = queue.pop(0)
            result.append(node)
            if node.val == key:
                ind = len(result) - 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    if len(result) -1 == ind:
        return -1

    return result[ind+1]



def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)

main()


# Connect Level Order Siblings

'''
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    queue = [root]

    while queue:
        length = len(queue)
        levelArray = []
        for i in range(length):
            node = queue.pop(0)
            levelArray.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == length - 1:
                node.next = None
        for j in range(len(levelArray) - 1):
            levelArray[j].next = levelArray[j+1]

    return root
            

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()


# Connect All Level Order Siblings 

'''
Given a binary tree, 
connect each node with its level order successor.
The last node of each level 
should point to the first node of the next level.
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None
 # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    # TODO: Write your code here
    queue = [root]

    while queue:
        levelArray = []
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            levelArray.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == length - 1 and len(queue) != 0:
                node.next = queue[0]
        for j in range(length - 1):
            levelArray[j].next = levelArray[j+1]

    return root
            
            




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()


# Right View of a Binary Tree

'''
Given a binary tree, return an array containing nodes in its right view.
 The right view of a binary tree is the set of nodes visible 
 when the tree is seen from the right side.

'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    # TODO: Write your code here
    queue = [root]

    while queue:
        levelArray = []
        length = len(queue)
        for _ in range(length):
            node = queue.pop(0)
            levelArray.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(levelArray[-1])
    return result

    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()

