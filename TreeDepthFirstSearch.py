# Binary Tree Path Sum

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
    
    find_paths_helper(root,sum,[],allPaths)
    
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
    
    return find_sum_of_path_numbers_helper(root,"", totalSum)


def find_sum_of_path_numbers_helper(root,currentNumber, sum):
    if root == None:
        return 0
    
    currentNumber += str(root.val)
    
    if root.left == None and root.right == None:
        sum += int(currentNumber)
        return sum
    
    # not necessary to delete the last letter from the string
    # currentNumber = currentNumber[:len(currentNumber)-1]
    
    return find_sum_of_path_numbers_helper(root.left, currentNumber,sum) + find_sum_of_path_numbers_helper(root.right, currentNumber,sum)
        

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
  
  return find_path_helper(root,"",sequence)

def find_path_helper(root,currentString, sequence):
    if root == None:
        return False
    
    currentString += str(root.val)
    
    if root.left == None and root.right == None:
        currentSequence = list(currentString)
        currentSequence = [int(x) for x in currentSequence]
        print(currentSequence)
        return currentSequence == sequence
    
    return find_path_helper(root.left, currentString,sequence) or find_path_helper(root.right, currentString,sequence)  

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

#added comment