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



# Rearrange a LinkedList (medium)

'''
Given the head of a Singly LinkedList, 
write a method to modify the LinkedList 
such that the nodes from the second half of 
the LinkedList are inserted alternately to the 
nodes from the first half in reverse order. 
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
 your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the 
input LinkedList should be modified in-place.

Example 1:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
Example 2:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
'''


print("rearrangeLinkedList")

def rearrangeLinkedList(head):
  middleNode = find_middle_of_linked_list(head)
  oneAfterMid = middleNode.next
  middleNode.next = None
  reversedList = reverseLinkedList(oneAfterMid)

  firstHalf = head
  secondHalf = reversedList


  while secondHalf != None:
    firstHalfNext = firstHalf.next
    secondHalfNext = secondHalf.next
    firstHalf.next = secondHalf
    secondHalf.next = firstHalfNext
    firstHalf = firstHalfNext
    secondHalf = secondHalfNext

  printLinkedList(head)
  return head


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  rearrangeLinkedList(head)
  


main()

# Cycle in a Circular Array (hard)
'''
Cycle in a Circular Array (hard)#
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example 1:

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
Example 2:

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
Example 3:

Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.


'''

def circular_array_loop_exists(arr):
  current = 0
  start = 0
  oneDirection = True

  for i in range(len(arr)):
    start, current  = i, i
    while True:
      if arr[current] > 0 and arr[start] > 0:
        if current + arr[current] > len(arr) - 1:
          difference = current + arr[current] - len(arr) - 1
          # because we array starts at 0
          current = difference - 1
        else:
          current += arr[current]
  
      elif arr[current] < 0 and arr[start] < 0:
        current += arr[current]
        if current < 0:
          current = len(arr) + current

      else:
        break

      if start == current:
        return True

  return False





def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()