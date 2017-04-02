from hw4 import *

def test_count_anagrams():
    assert count_anagrams(['19cs6', 'apple', '1s9c6', 'dog', 'cs1962', 'sc961'], 'cs196') == 3
    assert count_anagrams(['aabbcc', 'abcabc', 'abcdef', 'defghi'], 'golf') == 0

def test_happy_numbers():
    assert happy_numbers(8) == 2
    assert happy_numbers(15) == 4
    assert happy_numbers(10**5) == 14376

def test_reverse_dictionary():
    assert reverse_dictionary({}) == {}
    assert reverse_dictionary({'a': 1}) == {1: 'a'}
    assert reverse_dictionary({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
    alpha_map = {k: v
                 for k, v in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(ord('A'), ord('Z')+1))}
    reverse_alpha_map = {k: v
                         for k, v in zip(range(ord('A'), ord('Z')+1), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    assert reverse_dictionary(alpha_map) == reverse_alpha_map

def test_alphabet_finder():
    test = 'abcdefghijklmnopqrstuvwxyz'
    result = 'abcdefghijklmnopqrstuvwxyz'
    assert alphabet_finder(test) == result

    test = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
    result = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
    assert alphabet_finder(test) == result

    test = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
    result = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
    assert alphabet_finder(test) == result

    test = 'Wait, what if a sentence does not have all letters?'
    result = None
    assert alphabet_finder(test) == result

def test_anagram_of_palindrome():
	assert anagram_of_palindrome('civic') == True
	assert anagram_of_palindrome('ccivi') == True
	assert anagram_of_palindrome('rotator') == True
	assert anagram_of_palindrome('arortot') == True
	assert anagram_of_palindrome('asdf') == False
	assert anagram_of_palindrome('austin is dope') == False

def test_is_unique():
	assert is_unique('abcdef') == True
	assert is_unique('g') == True
	assert is_unique('hello world') == False
	assert is_unique('heLlo') == False


if __name__ == '__main__':
    test_reverse_dictionary()
    test_alphabet_finder()
    test_count_anagrams()
    test_happy_numbers()
    test_anagram_of_palindrome()
    test_is_unique()
    print "All Tests Passed!"
