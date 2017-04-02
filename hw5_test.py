from hw5 import *

def test_zero_sum():
    assert zero_sum([0, 1, 2, 3, 4, 5])
    assert zero_sum([10, 20, -20, 3, 21, 2, -6])
    assert zero_sum([4, 5, 9, -3, -2, 10, 3, -2, -11])
    assert not zero_sum([1, 2, 3, 4, 5, 1])
    assert not zero_sum([-1, -2, -3, -4, -5, -1])

    import random
    test_arr = [random.randrange(2, 10000) for i in range(100000)]
    test_arr[497] = -10
    test_arr[498] = 9
    test_arr[499] = 1
    assert zero_sum(test_arr)


def test_longest_incremental_sequence():
    assert longest_incremental_sequence([1, 2, 3, 4, 5]) == 5
    assert longest_incremental_sequence([4, 1, 2, 3, 5]) == 5
    assert longest_incremental_sequence(range(10000)) == 10000
    import random
    test = list(range(-10000, 10000))
    random.shuffle(test)
    assert longest_incremental_sequence(test) == 20000

def test_matrix_transpose():
    assert matrix_transpose([[1,2],[3,4],[5,6]]) == [[1, 3, 5], [2, 4, 6]]
    assert matrix_transpose([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]) == [['a', 'e', 'i', 'm'], ['b', 'f', 'j', 'n'], ['c', 'g', 'k', 'o'], ['d', 'h', 'l', 'p']]

def test_unique_rows():
    assert unique_rows([[1,2],[3,4],[1,2],[5,6]]) == [[1,2],[3,4],[5,6]]
    assert unique_rows([[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3],[1,0,0,1,3],[5,3,6,2,3]]) == [[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3]]

def test_magic_square():
    assert magic_square([[2,7,6],[9,5,1],[4,3,8]]) == True
    assert magic_square([[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3],[1,0,0,1,3],[5,3,6,2,3]]) == False
    assert magic_square([[8,1,6],[3,5,7],[4,9,2]]) == True

def test_nQueens():
    assert nQueens([[0,1,0],[0,0,0],[0,0,1]]) == True
    assert nQueens([[1,0,0],[0,0,0],[0,0,1]]) == False
    assert nQueens([[0,0,0],[0,0,0],[0,0,0]]) == True

def test_matrix_multiply():
    assert matrix_multiply([[1,4,6]], [[2,3],[5,8],[7,9]]) == [[64,89]]
    assert matrix_multiply([[4,8],[0,2],[1,6]], [[5,2],[9,4]]) == [[92,40],[18,8],[59,26]]
    assert matrix_multiply([[4,8],[0,2],[1,6]], [[5,2],[9,4],[0,1]]) == None


if __name__ == '__main__':
    #test_zero_sum()
    #test_longest_incremental_sequence()
    test_matrix_transpose()
    test_unique_rows()
    test_magic_square()
    test_nQueens()
    test_matrix_multiply()

    print "All tests passed!"
