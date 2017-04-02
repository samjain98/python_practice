#####################################################################################################
#
#   Node Class
#   Is a class representing a single node of the linked list. String together nodes to make a linked list.
#   self.data is a variable holding the data value
#   self.next is a variable that holds the pointer to the next node.
#
#####################################################################################################


class linked_node(object):
    # Node class for linked list implementation
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class tree_node(object):
    # Node class for BST implementation
    def __init__(self, data=None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


#####################################################################################################
#                                                                                                   #
#       HOMEWORK 8 PROBLEMS                                                                         #
#                                                                                                   #
#####################################################################################################

# Merge
#
# Given the head of two linked lists, return true if the linked lists merge, and false if they do not merge.
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head_a : node
#   Head of a linked list
#
# head_b : node
#   Head of another linked list
#
#
# Returns
# -------
#   Boolean

def isMerged(head_a, head_b):
	a = head_a
	b = head_b

	while (a.next != None):
		a = a.next

	while (b.next != None):
		b = b.next
	
	return a==b
# Find Merge Point
#
# Given the head of two linked lists that are merged, return the data at the node where the two lists merge.
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head_a : node
#   Head of a linked list
#
# head_b : node
#   Head of another linked list
#
# Returns
# -------
# int: data
#   data at merge node

def len_list(head):
	if head.next == None:
		return 1

	count = 1

	while head.next != None:
		count=count+1
		head = head.next

	return count

def findMerge(head_a, head_b):
    space = len_list(head_a) - len_list(head_b)

    if diff > 0:
        for i in xrange(1, space):
        	head_a = head_a.next
    
    if diff < 0:
        for i in xrange(1, -1*space):
        	head_b = head_b.next

    while head_a.next != None:
        if head_a==head_b:
            return head_a.data
        head_a = head_a.next
        head_b = head_b.next


# Cycle
#
# Given the head of a linked list, find out whether or not there is a cycle.
#
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# boolean :
#   True if there is a cycle, False if there is not

def hare(index1, index2):
	if index2.next == None or index2.next.next == None:
		return False

	if index1 == index 2:
		return True

	return hare(index1.next, index2.next.next)

def foundCycle(head):
    return hare(head,head.next)


# Find Odd
#
# Given the head node of a BST, return all odd data members of nodes in the tree in a list.
# Duplicates must be considered. Order does not matter.
#
#
# Example(s)
# ----------
# Input (tree representation):
#   head: node
#
#            3
#          /   \
#         2     5
#        / \   / \
#       4   3 8   7
#
# Output:
#   odds: list
#   [3,5,3,7]
#
#
# Parameters
# ----------
# head : node
#   Head of a BST
#
#
# Returns
# -------
# odds : list
#   list of odd data members in the tree
def oddSearch(head,arr):

	if head.right != None:
        oddSearch(head.right,arr)

    if head.left != None:
        oddSearch(head.left,arr)

    if (head.data % 2 == 1):
        arr.append(head.data)


def findOdd(head):
    arr = []
    if head == None:
        return arr
    oddSearch(head,arr)
    return arr