"""
same question as merge2sortedArray.py but input arrays are unsorted.

Solution:
we can simply append nums2 into nums1 since we’re allowed to modify nums1.
After that, the combined array will be unsorted, so we must sort it using Python’s built-in sort() method (which uses Timsort,
a hybrid of merge sort + insertion sort).
Finally, nums1 will contain all elements from both arrays in sorted (non-decreasing) order.

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()


nums1 = [3, 1, 4]
m = 3
nums2 = [5, 2, 6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print("Merged and sorted array:", nums1)


"""
⏱️ Time Complexity

Appending elements:
Adding n elements from nums2 to nums1 takes O(n) time.

Sorting combined array:
The total number of elements = m + n.
Sorting takes O((m + n) log(m + n)) time (Timsort complexity).


💾 Space Complexity

Python’s built-in .sort() is in-place, but Timsort can use temporary memory for merging — typically O(m + n) in the worst case.
✅ Space Complexity: O(m + n)

⚖️ Comparison with the Sorted Version
Case-Input Arrays-Time Complexity-Space Complexity-Algorithm
Sorted Arrays-Both sorted	O(m + n)	O(1)	Two-pointer merge (Merge step of Merge Sort)
Unsorted Arrays-Both unsorted	O((m + n) log(m + n))	O(m + n)	Combine + Sort (Timsort in Python)


"""
