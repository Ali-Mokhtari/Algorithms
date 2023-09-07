"""
Google Inerview Question
Author: Ali Mokhtari
GitHub: @Ali-Mokhtari
Date: September 2023

Q: Given an array of integers, find a pair of numbers that sum up to a given number.

Assumptions:
1. The array is not sorted
2. The array contains only integers
3. The array can contain duplicates
4. The array can contain negative numbers
5. The array can be empty

Return:
1. If a pair is found, return the pair
2. If a pair is not found, return None

Example:
numbers = [5, 7, 18, 9, 15, 5, 3, 15, 18]
required_sum = 12

return: (3, 9)

Solution:
1. Initialize an empty hash table for compliments (key: compliment, value: number).
   Note that the Python dictionarioes is the nearest builtin data structure to Hash tables.
   Lookup time for a dictionaries (hash tables) is O(1) compared to O(n) for a list.
2. Iterate through the array.
3. For each number, check if it is in the compliments dictionary.
4. If it is, return the pair
5. If it is not, calculate the compliment (sum_values - number) and add it to the dictionary.
6. If no pair is found, return None

Time Complexity: O(n)
"""


def find_pair(numbers, sum_value):
    if sum_value is None:
        return None
    # Step 1
    compliments = {}  # key: compliment, value: number
    # Step 2
    for number in numbers:
        # Step 3
        if number in compliments:
            # Step 4
            return (sum_value - number, number)
        else:
            # Step 5
            compliments[sum_value - number] = number
    # Step 6
    return None


def test_with_empty_array():
    numbers = []
    sum_value = 12
    pair = find_pair(numbers, sum_value)
    assert pair is None, "Test with empty array failed"


def test_with_positive_values():
    numbers = [18, 9, 5, 15, 7, 3, 18]
    sum_value = 12
    pair = find_pair(numbers, sum_value)
    assert pair == (5, 7), f"Test with positive values failed: {pair}"


def test_with_negative_values():
    numbers = [-5, -18, -9, -15, -5, -7, -15, -18]
    sum_value = -12
    pair = find_pair(numbers, sum_value)
    assert pair == (-5, -7), f"Test with negative values failed: {pair}"


def test_with_none_sum():
    numbers = [-5, -7, -18, -9, -15, -5, -3, -15, -18]
    sum_value = None
    pair = find_pair(numbers, sum_value)
    assert pair is None, "Test with None sum failed"


def test_with_all_same_numbers():
    numbers = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    sum_value = 10
    pair = find_pair(numbers, sum_value)
    assert pair == (5, 5), f"Test with all same numbers failed: {pair}"


if __name__ == "__main__":
    test_with_empty_array()
    test_with_positive_values()
    test_with_negative_values()
    test_with_none_sum()
    test_with_all_same_numbers()
    print("All tests passed")
