"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Solution:
We could use a set or dictionary to count occurrences,
but that would use extra space depending on n → ❌ violates O(1) space rule.

Understanding XOR operation:

The XOR operator (^) has special properties:
a ^ a = 0 → number cancels itself
a ^ 0 = a → XOR with 0 keeps the number

XOR is commutative and associative, meaning if we change the order of operations, the result remains the same.
So, if we XOR all numbers:
The pairs will cancel out (since x ^ x = 0)
Only the single number will remain.

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# Ask the user for input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# Create an object of the Solution class
sol = Solution()
# Call the method and print result
print("The single number is:", sol.singleNumber(nums))

##check with 1 2 2 1 4 as a user input


"""
Complexity Analysis

Time: O(n) → one pass through the array

Space: O(1) → only one variable used
"""
