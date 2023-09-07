"""
Interview Question
Author: Ali Mokhtari
GitHub: @Ali-Mokhtari
Date: September 2023

Q: Given two arrays, find whether there is common items.

Example:
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
return: False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
return: True

Assumptions:
1. The arrays length may not be equal.


Solution:
1. Convert the second array to a dictionary.
2. Iterate through the first array.
3. For each item in the first array, check if it is in the dictionary.
4. If it is, return True
5. If it is not, return False

Time Complexity: O(m+n) where m and n are the lengths of the arrays.
"""


def arr_to_dict(arr):
    dictionary = dict()
    if arr is None:
        return dictionary
    for item in arr:
        dictionary[item] = True
    return dictionary


def common_item(array1, array2):
    second_arr_dict = arr_to_dict(array2)
    if array1 is None:
        return False
    for item in array1:
        if item in second_arr_dict:
            return True
    return False


def test_with_empty_array():
    arr1 = []
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is False, 'Failed with empty array'


def test_with_no_common_items():
    arr1 = ['a', 'b', 'c', 'x']
    arr2 = ['z', 'y', 'i']
    assert common_item(arr1, arr2) is False, 'Failed with no common items'


def test_with_common_items():
    arr1 = ['a', 'b', 'c', 'x']
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is True, 'Failed with common items'


def test_with_repeated_items():
    arr1 = ['a', 'b', 'c', 'x', 'x']
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is True, 'Failed with repeated items'


def test_with_all_same_items():
    arr1 = ['a', 'a', 'a', 'a', 'a', 'a']
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is False, 'Failed with all same items'
    arr1 = ['a', 'a', 'a', 'a', 'a', 'a']
    arr2 = ['z', 'a', 'x']
    assert common_item(arr1, arr2) is True, 'Failed with all same items'


def test_with_none_array():
    arr1 = None
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is False, 'Failed with none array'


def test_with_none_item():
    arr1 = ['a', None, 'c', 'x']
    arr2 = ['z', 'y', 'x']
    assert common_item(arr1, arr2) is True, 'Failed with none item'
    arr1 = ['a', None, 'c', 'x']
    arr2 = ['z', 'y', None]
    assert common_item(arr1, arr2) is True, 'Failed with none item'


def test_with_numbers_and_strings():
    arr1 = ['a', 1, 'c', 'x']
    arr2 = ['z', '1', 'y']
    assert common_item(arr1, arr2) is False, 'Failed with numbers and strings'


if __name__ == '__main__':
    test_with_empty_array()
    test_with_no_common_items()
    test_with_common_items()
    test_with_repeated_items()
    test_with_all_same_items()
    test_with_none_array()
    test_with_none_item()
    print('All tests passed')
