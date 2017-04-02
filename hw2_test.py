from hw2 import *

######################################################################
# Test Cases
######################################################################

def testPangram():
    assert pangram('the quick brown fox jumps over the lazy dog') == True
    assert pangram('raining cats and lazy dogs') == False
    assert pangram('Bright vixens jump; dozy fowl quack') == True

def testPrimeTest():
    assert prime_test(13) == True
    assert prime_test(24) == False
    assert prime_test(99991) == True

def testCountVowels():
    assert count_vowels('aAaeeizzzzz') == 6
    assert count_vowels('computer science') == 6
    assert count_vowels('196.xyz') == 0

def testMostCommonChar():
    assert most_common_char('aaAAaBBbcc') == 'a'
    assert most_common_char('freshman honors') == 'r'
    assert most_common_char('siebel') == 'e'

def testFibonacci():
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(-1) == 1

def testAdvancedDivision():
    r1 = advanced_division(5, 6)
    assert type(r1) is float and r1 == 0.8333333333333334
    r2 = advanced_division(10, 5)
    assert type(r2) is int and r2 == 2
    r3 = advanced_division(2, 0.5)
    assert type(r3) is int and r3 == 4

def testPalindrome():
    assert palindrome('A man a plan a canal Panama') == True
    assert palindrome('I like doing homework') == False
    assert palindrome('racecar') == True

def testUnique():
    assert unique('banana') == False
    assert unique('Mississippi') == False
    assert unique('computers') == True

def testNthPalindromicPrime():
    assert nthPalindromicPrime(5) == 11
    assert nthPalindromicPrime(8) == 151
    assert nthPalindromicPrime(10) == 191    

# You can comment out tests for questions that you are not working on!
def testAll():
    testPangram()
    testPrimeTest()
    testCountVowels()
    testMostCommonChar()
    testFibonacci()
    testAdvancedDivision()
    testPalindrome()
    testUnique()
    testNthPalindromicPrime()
    print "All tests passed! "

testAll()    
