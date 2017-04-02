#####################################################################################################
#
#   Node Class
#   Is a class representing a single node of the linked list. String together nodes to make a linked list.
#   self.data is a variable holding the data value
#   self.next is a variable that holds the pointer to the next node.
#
#####################################################################################################

from hw7 import *

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

#####################################################################################################

def test_head():
	# Construction of the linked list
	head = Node(1,None) 						# assign head variable to the first node with data 1 and next = None.
	pointer = head 								# remember the head node
	head.next = Node(2,None) 					# Make another node, attach it to the first node
	head = head.next 							# Iterate to next node. This is very important.
	head.next = Node(3, None) 					# Make another node, attach it to the second node

	headPointer = add_head(pointer, 0)			# Call method with head of linked list and data s parameters
	iterate(headPointer)						# Use the iterate method to print nodes to console for sanity check and testing

	assert(True)								# Write your test case assertions starting here


def test_tail():
	pass

def test_position():
	pass

def test_reverse():
	pass

def test_skip():
	pass

def test_delete():
	pass

def test_duplicate():
	pass


if __name__ == '__main__':
    test_head()
    test_tail()
    test_reverse()
    test_skip()
    test_delete()
    test_duplicate()
    print "All tests passed!"


