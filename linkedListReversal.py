
# Reverse a LinkedList

'''
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
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

