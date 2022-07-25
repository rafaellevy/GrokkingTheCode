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
        return 
    
    currentNumber += str(root.val)
    
    if root.left == None and root.right == None:
        sum += int(currentNumber) 
    
    find_sum_of_path_numbers_helper(root.left, currentNumber,sum)
    find_sum_of_path_numbers_helper(root.right, currentNumber,sum)
    
    currentNumber = currentNumber[:len(currentNumber)-1]
    
    
    
    


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()