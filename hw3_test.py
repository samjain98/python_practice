from hw3 import*

def test_lazy_trainer():
    # Easy Cases
    assert lazy_trainer([]) == 0
    assert lazy_trainer([3, 2, 2]) == 10
    assert lazy_trainer([1, 2, 3, 4, 5]) == 36
    assert lazy_trainer([13, 7, 11, 1, 2, 10,
                         13, 12, 13, 8, 19, 10, 12, 0, 18, 14, 6, 7, 5, 13]) == 1524
    assert lazy_trainer([1, 8, 4, 7, 7, 7, 4,
                         7, 5, 7, 4, 8, 1, 4, 4, 0, 1, 0, 4, 5]) == 732
    assert lazy_trainer([9, 5, 0, 4, 6, 3, 8, 9, 7, 5, 5,
                         8, 1, 3, 9, 9, 2, 0, 5, 0, 4, 2, 0, 5, 4, 7, 1, 4, 5, 8]) == 1710
    # Medium Cases
    assert lazy_trainer([0 for i in range(100)] + [1]) == 101
    assert lazy_trainer(range(1, 101)) == 197026
    # "What is wrong with Shotaro" cases
    assert lazy_trainer(range(1, 100000)) == 192448869644925
    assert lazy_trainer(range(1, 999999)) == 192449390371901100
    assert lazy_trainer(range(1, 9999999)) == 192450019794009554500

def test_reverse_block():
    assert reverse_block(range(1,8), 3) == [3, 2, 1, 6, 5, 4, 7]
    assert reverse_block([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5]
    assert reverse_block([], 100) == []
    assert reverse_block(range(100), 100) == list(reversed(range(100)))
    assert reverse_block(range(1, 9), 3) == [3, 2, 1, 6, 5, 4, 8, 7]
    assert reverse_block(range(1, 25), 7) == [7, 6, 5, 4, 3, 2, 1,
                                              14, 13, 12, 11, 10, 9, 8,
                                              21, 20, 19, 18, 17, 16, 15,
                                              24, 23, 22]

def testNthLargestElement():
    assert nth_largest_element([3, 1, 5, 2, 4], 3) == 3
    assert nth_largest_element([-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], 5) == -183
    assert nth_largest_element([-788, 227, 22, -204, 569, -650, -692, -319, 378, -297], 9) == -692

def testSubsetSum():
    assert subset_sum([1, 5, 4, 3, 6, 2, 5, 17], 24) == True
    assert subset_sum([1, 18, 5], 10) == False
    assert subset_sum([-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], -797) == True
    assert subset_sum([-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], 1) == False

def testFindRing():
    assert(findRing([1, 3, 0, 1])) == 2
    assert(findRing([1,0])) == 2
    assert(findRing([1,2,1])) == 2
    assert(findRing([0])) == 1
    assert(findRing([1,2,3,4,5,6,7,8,9,2])) == 8

if __name__ == '__main__':
    test_reverse_block()
    test_lazy_trainer()
    testNthLargestElement()
    testSubsetSum()
    testFindRing()
    print "All tests passed!"
