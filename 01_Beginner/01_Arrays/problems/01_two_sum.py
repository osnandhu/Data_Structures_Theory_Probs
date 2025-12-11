"""
LeetCode 1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
"""


# ==================== YOUR SOLUTION ====================

def two_sum_brute_force(nums, target):
    """
    Brute Force Approach: Check all pairs

    Time Complexity: O(n²)
    Space Complexity: O(1)

    This is the FIRST solution you should think of!
    It's okay to start with brute force.
    """
    # TODO: Implement brute force (nested loops)
    pass


def two_sum_optimal(nums, target):
    """
    Optimal Approach: Hash Map

    Time Complexity: O(n)
    Space Complexity: O(n)

    Think: "What if I store numbers I've seen in a hash map?"
    For each number, check if (target - number) exists in map.
    """
    # TODO: Implement using hash map
    pass


# ==================== HINTS ====================
"""
Hint 1: For brute force, use two nested loops to check all pairs.

Hint 2: For optimal solution, think about what you need to find for each number.
        If current number is x and target is t, you need (t - x).

Hint 3: Use a dictionary to store {number: index} as you iterate.
        Before adding current number, check if (target - current) exists in dict.

Hint 4: Algorithm:
        1. Create empty dict
        2. For each number with index:
           a. Calculate complement = target - number
           b. If complement in dict: return [dict[complement], current_index]
           c. Store number and its index in dict
"""


# ==================== TESTING ====================

def test_two_sum():
    # Test brute force
    print("Testing brute force...")
    # assert sorted(two_sum_brute_force([2, 7, 11, 15], 9)) == [0, 1]
    # assert sorted(two_sum_brute_force([3, 2, 4], 6)) == [1, 2]
    # assert sorted(two_sum_brute_force([3, 3], 6)) == [0, 1]
    # print("✅ Brute force tests passed!")

    # Test optimal
    print("\nTesting optimal solution...")
    # assert sorted(two_sum_optimal([2, 7, 11, 15], 9)) == [0, 1]
    # assert sorted(two_sum_optimal([3, 2, 4], 6)) == [1, 2]
    # assert sorted(two_sum_optimal([3, 3], 6)) == [0, 1]
    # print("✅ Optimal solution tests passed!")


if __name__ == "__main__":
    test_two_sum()

    # After solving, answer these:
    """
    REFLECTION:
    1. Why is hash map approach faster than brute force?
       Answer: _______________________

    2. What is the trade-off of hash map approach?
       Answer: _______________________

    3. Can you solve it in O(1) space? Why or why not?
       Answer: _______________________

    4. What pattern did you learn from this problem?
       Answer: _______________________
    """
