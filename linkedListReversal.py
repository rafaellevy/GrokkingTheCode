
# Reverse a LinkedList

'''
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
'''


from __future__ import print_function
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
  p1 = None
  p2 = head
  i = 1
  if other:
    previous.next = p2
    while i < k and p2 != None:
      p2 = p2.next
      previous = previous.next
      i+=1
    return p2, previous

  i = 1
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
  # head is the last node of the reversed linkedlist and p3 is the head of the next sublist
  return head, p3, skip
  



def reverse_alternate_k_elements(head, k):
  skip = False
  current = head
  previous = None

  while current:
    previous, current, skip =  reverseList(previous,current,skip)


  return 


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


#main()

