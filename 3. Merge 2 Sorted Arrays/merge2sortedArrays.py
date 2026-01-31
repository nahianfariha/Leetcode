"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

solution:
1. We have to travel backward instead of forward to avoid overwriting elements in nums1.(ascending order)
2. We will compare the last elements of both arrays (as they are already in ascending order) and place the larger one at the end of nums1.
3. size= m=n, then indices will be m+n-1 for the sorted array, m-1 for nums1 and n-1 for nums2.
4.idx = m+n-1 , i=m-1, j=n-1
5. j-- and idx-- and compare

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1


# Take input from user
m = int(input("Enter the number of elements in the first array: "))
nums1 = list(
    map(
        int,
        input(f"Enter {m} elements of the first array in ascending order: ").split(),
    )
)

n = int(input("Enter the number of elements in the second array: "))
nums2 = list(
    map(
        int,
        input(f"Enter {n} elements of the second array in ascending order: ").split(),
    )
)

# Extend nums1 to hold extra space for nums2
nums1.extend([0] * n)

# Merge the arrays
sol = Solution()
sol.merge(nums1, m, nums2, n)

# Output
print("Merged and sorted array:", nums1)

"""
# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
"""

"""
Time Complexity Analysis:
We have two arrays: nums1 of size m (valid elements) and nums2 of size n.
In the worst case, we compare each element from both arrays exactly once while merging.
while i >= 0 and j >= 0 → at most m + n comparisons.
while j >= 0 → at most n assignments (in case all remaining elements of nums2 are smaller than nums1).
✅ Therefore, total time complexity = O(m + n).
This is linear, which is optimal because we must look at all elements at least once.

Space Complexity
We do not create any new array.
All merging is done in-place in nums1.
✅ Therefore, space complexity = O(1) (constant extra space).

"""
