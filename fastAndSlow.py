from ctypes import pointer


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  # TODO: Write your code here
    fast = head
    slow = head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()


def find_cycle_length(head):
  fast = head
  slow = head
  newPointer = slow
  count = 0


  while fast != None and fast.next != None:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        newPointer = slow
        break

  while True:
    newPointer = newPointer.next
    count += 1
    if newPointer == slow:
      break
  return count 

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()

def find_cycle_start(head):
  length = find_cycle_length(head)

  p1 = head
  p2 = head

  for _ in range(length):
    p2 = p2.next

  while p1 != p2:
    p1 = p1.next
    p2 = p2.next

  return p1

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

print("HAPPY NUMBER")

def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square(slow)
    fast = find_square(find_square(fast))
    if slow == fast:
      if slow == 1:
        return True
      else:
        return False




def find_square(num):
  sum = 0
  while num > 0:
    last_digit = num % 10
    sum += last_digit * last_digit
    num = num // 10
  return sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()

print("FIND MIDDLE OF LINKED LIST")

def find_middle_of_linked_list(head):
  fast = head
  slow = head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()


# Palindrome LinkedList

'''
Given the head of a Singly LinkedList, write a 
method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input 
LinkedList should be in the original form once the algorithm is finished. 
The algorithm should have O(N) time complexity where 'N' is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''

def is_palindromic_linked_list(head):
  middleNode = find_middle_of_linked_list(head)
  reversedListHead = reverseLinkedList(middleNode)
  right = reversedListHead
  left = head

  while left != middleNode:
    if left.value == right.value:
      left = left.next
      right = right.next
    else:
      printLinkedList(reversedListHead)
      printLinkedList(head)
      reverseLinkedList(reversedListHead)
      printLinkedList(head)
      return False
  
  printLinkedList(reversedListHead)
  printLinkedList(head)
  reverseLinkedList(reversedListHead)
  printLinkedList(head)
  
  return True

def reverseLinkedList(node):
  p0 = None
  p1 = node
  
  while p1 != None:
    p2 = p1.next
    p1.next = p0
    p0 = p1
    p1 = p2
  #return the head
  return p0


def printLinkedList(head):
  while head:
    print(f"{head.value}->",end=" ")
    head = head.next
  print()
  

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

