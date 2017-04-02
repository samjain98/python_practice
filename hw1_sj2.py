###############################################################################
#
#   HW1.py
#   CS196 FA16
#   Functions, Strings, Types
#   Released: August 31, 2016
#   Due: September 6th, 7pm
#
###############################################################################


###############################################################################
# CSVify
#
# Often, you will need to take some sort of data and condition it to be in a
# particular format. In this case, we will take a long string and manipulate it
# to behave like a comma-separated-value file. To do this, you should remove
# the whitespace between words in the string and RETURN the conditioned string
# whilst keeping intact line breaks.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'the quick  brown   fox\njumped    over the  lazy   dog'
#   Should replace all the whitespace between the words with commas
#   Output:
#   'the,quick,brown,fox\njumped,over,the,lazy,dog'
#
# Parameters
# ----------
# raw_str : str
#   A (potentially) multilined string containing words, newlines, and
#   whitespace
#
# Returns
# -------
# str
#   The comma-separated string
#
def csvify(raw_str):
    """
    Removes whitespaces and replaces with commas

    >>> print csvify('the quick  brown   fox\\njumped    over the  lazy   dog')
    the,quick,brown,fox
    jumped,over,the,lazy,dog
    >>> print csvify('subject course   term\\n CS 196    Fall16\\nCS 125     Fall16')
    subject,course,term
    CS,196,Fall16
    CS,125,Fall16
    """
    # Your code goes here!
    # Remove me after starting
    save_lines = raw_str.replace("\n", "\\n")
    comma_string = ','.join(save_lines.split())
    newline_string = comma_string.replace("\\n", "\n")
    return newline_string

###############################################################################
# To_Binary
#
# RETURN a string representing the integer parameter in binary.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 23
#   The binary representation of 23 is 10111
#   Output:
#   '10111'
#
# Parameters
# ----------
# num : integer
#   A positive integer
#
# Returns
# -------
# str
#   String representation of the integer using the fewest number of characters
#   as possible. (No zero padding)
#
def to_binary(num):
    """
    Represents an integer in binary as a string of 0's and 1's

    >>> print to_binary(23)
    10111
    >>> print to_binary(123456789)
    111010110111100110100010101
    """
    # Your code goes here!

    #[2:] removes the 0b that comes at the beginning of the bin return
    return bin(num)[2:]


###############################################################################
# Sum List
#
# Return an integer that represents the sum of the string list
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "20,4,12"
#   The summation of 20, 4, and 12 is 36.
#   Output:
#   36
#
# Parameters
# ----------
# nums : str
#   Comma separated string list of integers
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def sum_list(arr):
    """
    Sums the list of strings into an int

    >>> print sum_list("1,2,3,4")
    10
    >>> print sum_list("4,4")
    8
    """
    # Your code goes here!

    spaced = arr.replace(',', ' ')
    vals = spaced.split()

    total = 0

    for val in vals:
    	total += int(val)

    return total


###############################################################################
# Remove Given String
#
# You will be given a string and a removal string, and you will
# need to remove the removal string (both upper and lower case)
# from the string and then return your result.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ("." , "Hello. I'm Frodo.")
#   You should remove all periods.
#   Output:
#   "Hello I'm Frodo"
#
# Parameters
# ----------
# remove_str : str
#   String to remove
# word : str
#   Word to remove character from
#
# Returns
# -------
# str
#   The string you removed the character from
#
def remove_given_str(remove_str, word):
    """
    Removes remove_str from word

    >>> print remove_given_str("H","Harry is hot in Hogwarts")
    arry is ot in ogwarts
    >>> print remove_given_str("oops","Whoopsie, I made an oopsie. Oops!")
    Whie, I made an ie. !
    """
    import re

    # Your code goes here!
    return re.sub( remove_str, '', word, flags=re.I)




###############################################################################
# To Integer
#
# Take a list of booleans and return an integer made from its binary
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "true,false,true,false"
#   The decimal equivalent of 1010 is 10
#   Output:
#   10
#
# Parameters
# ----------
# arr : str
#   Comma separated string list of booleans
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def to_int(arr):
    """
    Converts a list of booleans into an integer

    >>> print to_int("true,false,true,true")
    11
    >>> print to_int("true,false,false,false,true")
    17
    """
    # Your code goes here!

    ones = arr.replace('true', '1')
    zeroes = ones.replace('false', '0')
    number = zeroes.replace(',', '')

    return int(number,2)



###############################################################################
# Carpet Weaving
#
# Given a width and height, print out a carpet design with alternating diagonal rows of O's and X's
# Define and use a helper function to decide if a carpet square should be an O or X.
#
# Example(s)
# ----------
# Example 1:
#   Input: 4,3
#   Width of 4 and height of 3
#   Output:
#   XOXO
#   OXOX
#   XOXO
#
# Example 2:
#   Input: 2,2
#   Width of 2 and height of 2
#   Output:
#   XO
#   OX
#
# Parameters
# ----------
# width : int
#   Width of carpet
# height : int
#   Length of carpet
#
# Prints
# -------
# The finished carpet
#

def x_or_o(row, col):

    if (row%2 == 0 and col%2 == 0):
        return "X"
    elif (row%2 == 1 and col%2 == 1):
        return "X"
    else:
        return "O"

def weave_carpet(width, height):
    """
    Prints a design width alternating diagonal rows of O's and X's
    Must use a helper function

    >>> weave_carpet(2,3)
    XO
    OX
    XO
    """
    # Your code goes here!
    line = ""

    for row in range (0, height):
        for col in range (0, width):
            line += x_or_o(row, col)
        print line
        line = ""


###############################################################################
# Caesar Cipher
#
# Caesar Cipher is an old way to encrypt secret messages across two users,
# by using a number to each word in the sentence by.
#
# We will be using the alphabet A-Z, a-z, then 0-9, which means the alphabet you will be shifting
# through will contain 62 characters.
#
# For reference here is the alphabet you will be shifting through:
#
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 0 1 2 3 4 5 6 7 8 9
#
# where A is the first character in the alphabet, B is the second, C is the third, and so on.
# Please ignore any characters not in the alphabet, and keep them the same as before.
#
# Given a string and the number of shifts, RETURN the resulting string of the caesar cipher operation.
#
# Example(s)
# ----------
# Example 1:
#   Input: caesar_cipher('Test.', 15)
#   You will need to encode the string 'Test.', by shifting right by 15.
#   T + 15 = i
#   e + 15 = t
#   s + 15 = 7
#   t + 15 = 8
#   . -> . (Keep everything not in the alphabet out)
#   Output:
#   'it78.'
#
# Parameters
# ----------
# sentence : String
#   The sentence that must be encoded.
# shifts : Int
#   The number of right shifts that should be done on the string.
#
# Returns
# -------
# String
#   The Caesar Cipher of the sentence shifted right by shift.
#
import re

def caesar_cipher(sentence, shifts):
    key = []

    for x in range (0, 26):
        key.append( chr(x + 65) )

    for x in range (26, 52):
        key.append( chr(x + 71) )

    for x in range (52, 62):
        key.append( chr(x - 4) )
        
    new_sentence = ""
    for c in sentence:
        if (re.match("[A-Za-z0-9]", c) ):
            pos = key.index(c)
            adjustment = shifts
            
            while (pos + adjustment > 61):
                adjustment -= (62-pos)
                pos = 0
            
            pos += adjustment
            new_sentence += key[pos]
            
        else:
            new_sentence += c
    
    return new_sentence 

###############################################################################
# Mom and Dad
#
# Given a string, RETURN True if the continous substring 'mom' appears the same number of times
# as the continous substring 'dad'. Otherwise, RETURN false.
#
# The input will always be given as a lower case string. You do not have to worry about upper cases.
#
# Example(s)
# ----------
# Example 1:
#   Input: mom_and_dad('momdad')
#   We have the substring going from 'mom' and 'dad'. There is one each.
#
#   Output:
#   True
#
# Example 2:
#   Input: mom_and_dad('momomdad')
#   We have the string 'mom' from the first part of the string (mom omdad)
#   However, we have another occurance of 'mom' right after. (mo mom dad)
#   Next we only have 1 occurance of 'dad'.
#
#   Output:
#   False
#
# Parameters
# ----------
# string: String
#   String representing the sentence to find the number of occurances of 'mom' and 'dad'.
#   The string will always be given as a lowercase.
#
# Returns
# -------
# Bool
#   Boolean representing whether or not the same number of 'mom' and 'dad' occur in the string.
def mom_and_dad(string):
    """
    Given a string, RETURN True if the number of appearnces of 'mom' and 'dad' are the same.

    >>> mom_and_dad('momdad')
    True
    >>> mom_and_dad('momomdad')
    False
    >>> mom_and_dad('mom091213aiomomdadmomoomomomdadadfishsdadandwich')
    False
    >>> mom_and_dad('momomdadad')
    True
    """
    # Your code goes here!
    dad_count = 0
    mom_count = 0
    for x in range (0, len(string)    - 2):
        if (string[x:x+3] == "mom"):
            mom_count+=1
        elif (string[x:x+3] == "dad"):
            dad_count+=1

    if mom_count == dad_count:
        return True
    else:
        return False



if __name__ == '__main__':
    # Students can test this just by running the script
    # With the -v argument, they can find out the ones they got wrong.
    import doctest
    doctest.testmod()
