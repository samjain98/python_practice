#Sameer Jain CS 196 
#Counting Anagrams
#
# Write a function that, given a string, will return the number of instances
# of anagrams of that string in the provided list of strings.
#
# Two strings are anagrams when they have the exact same number and frequency
# of characters, and order is ignored. Taking a string and rearranging its
# characters generates anagrams of that string. So, 'listen' and 'silent' are
# anagrams.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ['19cs6', 'apple', '1s9c6', 'dog', 'cs1962', 'sc961'], 'cs196'
#   Output:
#   3
#
# Example 2:
#   Input: ['aabbcc', 'abcabc', 'abcdef', 'defghi'], 'golf'
#   Output:
#   0
#
# Parameters
# ----------
# arr : List[str]
#   A list of strings
#
# uniq : str
#   The string to find anagrams of
#
# Returns
# -------
# int
#   The number of strings in arr that are exact anagrams of uniq.
#

def create_dict_from_string(word): #doing this frequently enough to create a method
    wordDict = {}

    for character in word:
        wordDict[character] = word.count(character) #value in dictionary not important

    return wordDict

def count_anagrams(arr, uniq):
	uniqDict = create_dict_from_string(uniq) #convert the word into a dict
	matchCounter = 0

	for word in arr:
		tempDict = create_dict_from_string(word)
		if (tempDict == uniqDict): 
			matchCounter += 1 #count all the matches, since dict is unordered
	
	return matchCounter


# Happy Numbers
#
# A happy number is a positive integer with the following characteristic: if we
# take ths sum of the square of its digits to get another number, and take the
# sum of the squares of that number and continue this process, we eventually
# get the number 1. If a number is not happy, we will get stuck in a cycle that
# does not include the number 1.
#
# Your task is to find the number of happy numbers between 0 and the given
# integer n.
#
# Calculation Example:
# 19 is a happy number.
# 19 -> 1^2 + 9^2 = 1 + 81 = 82
# 82 -> 8^2 + 2^2 = 64 + 4 = 68
# 68 -> 6^2 + 8^2 = 36 + 64 = 100
# 100 -> 1^2 + 0^2 + 0^2 = 1.
#
# Example(s)
# ----------
# Example 1:
#   Input: 8
#   Between 0 and 8, numbers 1 and 7 are happy numbers
#   Output:
#   2
#
# Example 2:
#   Input: 15
#   Between 0 and 25, numbers 1, 7, 10, and 13 are happy numbers
#   Output:
#   4
#
# Parameters
# ----------
# n : int
#   The high end of the range you need to check for happy numbers
#
# Returns
# -------
# int
#   The number of happy numbers between 0 and n (exclusive)
#

def calculate_digit_square_sum(n):
	sum = 0;

	while (n > 0): #calculate the sum of square of digits
		sum += (n % 10)*(n%10)
		n/=10

	return sum

def is_happy_number(n):
    path = {}
    digitSum = n

    while (True):
        digitSum = calculate_digit_square_sum(digitSum) #calc the sum

        if (digitSum == 1): #it is a happy number if it reaches 1
            return True
        elif (digitSum in path): #if it hits an old number it fails
            return False
        else: #it continues if it's an unseen number
            path[digitSum] = 1


def happy_numbers(n):
	if (n == 1):
		return 1

	counter = 0 #count all the happy numbers using the methods
	for iterator in xrange(n):
		if (is_happy_number(iterator)):
			counter +=1

	return counter



# Reverse Dictionary
#
# Given a dictionary, return a new dictionary with keys and values swapped.
#
# Example(s)
# ----------
# Example 1:
#   Input: {'a': 1, 'b': 2}
#   We will need to swap the keys and values.
#   Output:
#   {1: 'a', 2: 'b'}
#
# Parameters
# ----------
# d : dict
#   The dictionary you will be required to swap
#
# Returns
# -------
# dict
#   The dictionary given, but reversed
#
def reverse_dictionary(d):
	newDict = {} #create new dictionary
	for key in d:
		newDict[d[key]] = key #assign value as key, key as value

	return newDict

# Alphabet Finder
#
# Given a string, find the shortest prefix where all letters of the alphabet first appears.
# If there is no prefix such that all the letters of the alphabet appear, return None.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdefghijklmnopqrstuvwxyz'
#   This is just the alphabet.
#   Output:
#   'abcdefghijklmnopqrstuvwxyz'
#
# Example 2:
#   Input: 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
#   The alphabet first appears where the first z appears.
#   Output:
#   'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
#
# Example 3:
#   Input: 'Wait, what if a sentence does not have all letters?'
#   There is no alphabet in the input.
#   Output:
#   None
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# str
#   The prefix that the alphabet first appears.
# None
#   There is no complete alphabet.
#
def alphabet_finder(sentence):
    lowercaseSentence = sentence.lower()
    aValue = 97
    zValue = 122
    alphabetLength = 26

    letterDict = {}
    sentenceSubstring = ""; #store the substring in a variable
    for character in lowercaseSentence:

        sentenceSubstring += character #add to substring

        if ( ord(character) >= aValue and ord(character)<= zValue):
            letterDict[character] = 1 #if it's a letter, add it to the dict
        
        if (len(letterDict) == alphabetLength):
            return sentenceSubstring #when the dict reaches 26, we've completed the alphabet
    
    return None
	    




# Anagram of Palindrome
#
# Given a string, find out if it is an anagram of a palindrome.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'ivicc'
#   Output: True
#   Anagram of 'civic', which is a palindrome.
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is an anagram of a palindrome, False otherwise
#
def anagram_of_palindrome(word):

    wordDict = create_dict_from_string(word)
    singleOdd = 0; #only one odd character in odd lengthed words

    if ( len(word) %2 == 0 ): #make sure all character counts are even in even word
        for key in wordDict:
            if (wordDict[key] %2 != 0):
                return False
    else:
        for key in wordDict: #only allow one odd character in odd word
            if (wordDict[key]%2 != 0 and singleOdd > 0):
                return False
            elif (wordDict[key]%2 != 0):
                singleOdd += 1

    return True



# is unique
#
# Given a string, find out if it is made of only unique characters. Characters are not case sensitive,
# so 'l' and 'L' are considered to be the same character.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdef'
#   Output: True
#   'abcdef' is made of unique characters
#
# Example 2:
#   Input: 'hello worLd'
#   Output: False
#   There are 3 'l's in 'hello world', therefore it is not made of unique characters.
#
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is made of unique characters, false otherwise.
#
def is_unique(word):
    lowercaseWord = word.lower()
    alphabetDict = {}
    aValue = 97
    zValue = 122

    for character in lowercaseWord:
    	if ( ord(character) >= aValue and ord(character)<= zValue):
    		if ( character in alphabetDict ): #check if letter already existed
    			return False

    		else:
    			alphabetDict[character] = 1 #add to alphabet dictionary if letter was not there before

    return True


