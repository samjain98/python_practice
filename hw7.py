#####################################################################################################
#
#   Node Class
#   Is a class representing a single node of the linked list. String together nodes to make a linked list.
#   self.data is a variable holding the data value
#   self.next is a variable that holds the pointer to the next node.
#
#####################################################################################################


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


#####################################################################################################
#                                                                                                   #
#       HOMEWORK 7 PROBLEMS                                                                         #
#                                                                                                   #
#####################################################################################################

# ITERATE
#
# Given the head of a linked list, iterate through the linked list and print the values.
#
# Note: THIS IS A COMPLETED EXAMPLE FOR YOU
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       1, 2, 3, 4
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
#   None, prints values
#
def iterate(head):
    while(head != None):
        print head.data
        head = head.next

# REVERSE
#
# Given the head of a linked list, return a linked list that is reversed.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 4 -> 3 -> 2 -> 1 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
# 1 2 3 4 5 
#
# Returns
# -------
# head: node
#   Head of the reversed linked list
def reverse(head):

        prev = None
        current = head

        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


# SKIP
#
# Given the head of a linked list, return a linked list with every other node
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 3 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# head : node
#   Head of a linked list with every other node
def skip(head):

	unchanged_head = head

	while head.next != None and (head.next).next != None:
		head.next = (head.next).next
		head = head.next

	if head.next != None and (head.next).next == None:
		head.next = None

	return unchanged_head

# TAIL
#
# Given the head of a linked list and an int, append a node with the int data to the tail of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 5 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the tail node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the tail
  def add_tail(head, n):
      
      if(head == None):
          return Node(n,None)

      else:
          pointer = head
          while(head.next != None):
              head = head.nex t
          head.next = Node(n, None)

      return pointer


# HEAD
#
# Given the head of a linked list and an int, append a node with the int data to the head of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 5 -> 1 -> 2 -> 3 -> 4 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the head node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the head
def add_head(head, n):
	if (head == None):
		return Node(n, None)
	else:
		return Node(n, head)

# ADD
#
# Given the head of a linked list, an int : data and an int : i, add a node with int : data to the i'th position in the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 5 -> 4 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# data : int
#   data for the tail node
#
# i : int
#   position of the new node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node in the i'th position of the linked list
def add_position(head, data, i):

	unchanged_head = head

	if (i == 0):
		return Node(data, unchanged_head)

	counter = 1

	while (counter < i):
		head = head.next
		counter+=1

	holder = head.next
	head.next = Node (data, holder)

	return unchanged_head	

# DELETE
#
# Given the head of a linked list, an int : i, delete the i'th node in the linked list and return the new linked list.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# i : int
#   position of the node to delete
#
# Returns
# -------
# head : node
#   Head of a linked list with the node in the i'th position of the linked list deleted
def delete(head, i):

	if i == 0:
		head = head.next
		return head

	else:
		counter = 0
		while head != None:
			if i == counter + 1:
				head.next = (head.next).next
				return head
			else:
				counter += 1
				head = head.next
	return head

# DELETE_DUPLICATE
#
# Given the head of a linked list, delete all consecutive duplicate nodes in the linked list. Only consider CONSECUTIVE duplicates.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 2 -> 3 -> 4 -> 2 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 2 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# Returns
# -------
# head : node
#   Head of a linked list with the node with consecutive duplicates deleted.
def deleteDuplicate(head):

    current = head
	if (head == None):
		return head
	while current.next != None:
            if current.data == current.next.data:
                current.next = (current.next).next
            else:
               current = current.next



