
# Reverse a LinkedList

'''
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
'''


from __future__ import print_function
from collections import deque
from logging import _Level
import queue
from turtle import left
from unittest import skip


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
      
    print()


def reverse(head):
  p1 = None
  p2 =  head

  while p2 != None:
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3
  
  return p1


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

#Reverse a Sub-list (medium)

'''
Given the head of a LinkedList and two positions p and q, 
reverse the LinkedList from position p to q.

'''

def reverse_sub_list(head, p, q):
  # TODO: Write your code here

  leftNode = head
  i = 1
  while i < p - 1:
    leftNode = leftNode.next
    i += 1
  
  if p == 1:
    startNode = leftNode
  else:
    startNode = leftNode.next


  endNode = head
  j = 1
  while j < q:
    endNode = endNode.next
    j += 1

  if endNode.next is None:
    rightNode = endNode
  else:
    rightNode = endNode.next

  
  p1 = None
  p2 = startNode
  while p1 != endNode:
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3

  if startNode != leftNode:
    leftNode.next = endNode
  if endNode != rightNode:
    # the start of the sublist - when reversed, this is the end of the sublist.  
    # We need to connect the end with the right node
    startNode.next = rightNode

  if p == 1:
    return p1
  else:
    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

# Reverse every K-element Sub-list (medium)

'''
Given the head of a LinkedList and a number k, 
reverse every k sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than k elements, reverse it too.

'''

# start is the start node of the sublist
def reverse_sublist_size_k(start, k, previous):
  p1 = None
  p2 = start
  while k > 0 and p2 != None:
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3
    k -= 1
  
  start.next = p3
  if previous != None:
    previous.next = p1

  return p3, start

def reverse_every_k_elements(head, k):
  # TODO: Write your code here
  newHead = head
  i = 1
  while i < k:
    newHead = newHead.next
    i+=1

  currentNode = head
  previousEnd = None
  while currentNode != None:
    currentNode, previousEnd = reverse_sublist_size_k(currentNode, k, previousEnd)

  return newHead


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


# Reverse alternating K-element Sub-list 

'''
Given the head of a LinkedList and a number k, 
reverse every alternating k sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than k elements, reverse it too.
'''

def reverseList(head, previous,k,skip):
  i = 1
  if skip == True:
    while i <= k and head is not None:
      head = head.next
      i += 1
      previous = previous.next
    skip = False

    return previous, head, skip

  p1 = None
  p2 = head

  while i <= k and p2 != None:
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3
    i += 1
  # connect the left side of the linkedlist to reversed sublist if exists
  if previous != None:
    previous.next = p1
  #connect the reversed sublist to right side of the linked list
  head.next = p3
  if not skip:
    skip = True
  else:
    skip = False
  # head is the last node of the reversed linkedlist and p3 is the head of the next sublist
  return head, p3, skip
  



def reverse_alternate_k_elements(head, k):
  newHead = head
  i = 1
  while i < k:
    newHead = newHead.next
    i += 1
    
  skip = False
  current = head
  previous = None

  while current:
    previous, current, skip =  reverseList(current,previous,k,skip)

  
  return newHead

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


# Rotate a LinkedList (medium)

'''
Given the head of a Singly LinkedList and a number k, 
rotate the LinkedList to the right by k nodes.
'''

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  # find the length and the last node of the list
  last_node = head
  list_length = 1
  while last_node.next is not None:
    last_node = last_node.next
    list_length += 1

  last_node.next = head  # connect the last node with the head to make it a circular list
  rotations %= list_length  # no need to do rotations more than the length of the list
  skip_length = list_length - rotations
  last_node_of_rotated_list = head
  for i in range(skip_length - 1):
    last_node_of_rotated_list = last_node_of_rotated_list.next

  # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
  head = last_node_of_rotated_list.next
  last_node_of_rotated_list.next = None
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()

