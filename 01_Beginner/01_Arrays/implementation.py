"""
Array Implementation & Practice
Complete the functions below to practice array operations.
"""


def find_max(arr):
    """
    Find the maximum element in the array.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Maximum element in the array

    Example:
        >>> find_max([3, 1, 4, 1, 5, 9, 2])
        9
    """
    # TODO: Implement this
    pass


def reverse_array(arr):
    """
    Reverse the array in-place.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List to reverse

    Returns:
        None (modifies array in-place)

    Example:
        >>> arr = [1, 2, 3, 4, 5]
        >>> reverse_array(arr)
        >>> arr
        [5, 4, 3, 2, 1]
    """
    # TODO: Implement using two pointers
    pass


def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array in-place.
    Return the length of the array with unique elements.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Sorted list of integers

    Returns:
        Length of array with unique elements

    Example:
        >>> arr = [1, 1, 2, 2, 3, 4, 4]
        >>> length = remove_duplicates(arr)
        >>> arr[:length]
        [1, 2, 3, 4]
    """
    # TODO: Implement using two pointers
    pass


def rotate_array(arr, k):
    """
    Rotate array to the right by k steps.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List to rotate
        k: Number of steps to rotate

    Returns:
        None (modifies array in-place)

    Example:
        >>> arr = [1, 2, 3, 4, 5]
        >>> rotate_array(arr, 2)
        >>> arr
        [4, 5, 1, 2, 3]

    Hint: Use reverse operations!
    1. Reverse entire array
    2. Reverse first k elements
    3. Reverse remaining elements
    """
    # TODO: Implement
    pass


def find_missing_number(arr, n):
    """
    Given an array containing n distinct numbers from 0 to n,
    find the missing number.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of n numbers from 0 to n with one missing
        n: The range (0 to n)

    Returns:
        The missing number

    Example:
        >>> find_missing_number([3, 0, 1], 3)
        2
        >>> find_missing_number([0, 1], 2)
        2

    Hint: Use sum formula: sum(0 to n) = n * (n + 1) / 2
    """
    # TODO: Implement
    pass


def move_zeros(arr):
    """
    Move all zeros to the end while maintaining order of non-zero elements.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        None (modifies array in-place)

    Example:
        >>> arr = [0, 1, 0, 3, 12]
        >>> move_zeros(arr)
        >>> arr
        [1, 3, 12, 0, 0]

    Hint: Use two pointers - one for reading, one for writing non-zeros
    """
    # TODO: Implement
    pass


def find_second_largest(arr):
    """
    Find the second largest element in the array.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers (length >= 2)

    Returns:
        Second largest element

    Example:
        >>> find_second_largest([12, 35, 1, 10, 34, 1])
        34
    """
    # TODO: Implement (single pass!)
    pass


def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a new sorted array.

    Time Complexity: O(n + m) where n, m are lengths of arrays
    Space Complexity: O(n + m) for the result array

    Args:
        arr1: First sorted list
        arr2: Second sorted list

    Returns:
        New merged sorted list

    Example:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]

    Hint: Use two pointers, one for each array
    """
    # TODO: Implement
    pass


# ==================== TESTING ====================

def test_find_max():
    assert find_max([3, 1, 4, 1, 5, 9, 2]) == 9
    assert find_max([1]) == 1
    assert find_max([-5, -2, -10, -1]) == -1
    print("✅ find_max tests passed!")


def test_reverse_array():
    arr1 = [1, 2, 3, 4, 5]
    reverse_array(arr1)
    assert arr1 == [5, 4, 3, 2, 1]

    arr2 = [1]
    reverse_array(arr2)
    assert arr2 == [1]

    arr3 = [1, 2]
    reverse_array(arr3)
    assert arr3 == [2, 1]
    print("✅ reverse_array tests passed!")


def test_remove_duplicates():
    arr = [1, 1, 2, 2, 3, 4, 4]
    length = remove_duplicates(arr)
    assert arr[:length] == [1, 2, 3, 4]

    arr2 = [1, 1, 1]
    length2 = remove_duplicates(arr2)
    assert arr2[:length2] == [1]
    print("✅ remove_duplicates tests passed!")


def test_rotate_array():
    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 2)
    assert arr == [4, 5, 1, 2, 3]

    arr2 = [1, 2, 3]
    rotate_array(arr2, 4)  # k > n
    assert arr2 == [3, 1, 2]
    print("✅ rotate_array tests passed!")


def test_find_missing_number():
    assert find_missing_number([3, 0, 1], 3) == 2
    assert find_missing_number([0, 1], 2) == 2
    assert find_missing_number([9,6,4,2,3,5,7,0,1], 9) == 8
    print("✅ find_missing_number tests passed!")


def test_move_zeros():
    arr = [0, 1, 0, 3, 12]
    move_zeros(arr)
    assert arr == [1, 3, 12, 0, 0]

    arr2 = [0]
    move_zeros(arr2)
    assert arr2 == [0]
    print("✅ move_zeros tests passed!")


def test_find_second_largest():
    assert find_second_largest([12, 35, 1, 10, 34, 1]) == 34
    assert find_second_largest([10, 5]) == 5
    print("✅ find_second_largest tests passed!")


def test_merge_sorted_arrays():
    assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_arrays([1], []) == [1]
    print("✅ merge_sorted_arrays tests passed!")


if __name__ == "__main__":
    print("Running tests...\n")

    # Uncomment tests as you implement each function
    # test_find_max()
    # test_reverse_array()
    # test_remove_duplicates()
    # test_rotate_array()
    # test_find_missing_number()
    # test_move_zeros()
    # test_find_second_largest()
    # test_merge_sorted_arrays()

    print("\n🎉 All tests passed! You're mastering arrays!")
