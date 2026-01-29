class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        ans = []  # This will store the answer: [repeated, missing]
        n = len(grid)  # Size of the n x n grid
        a = b = 0  # 'a' will store the repeated number, 'b' the missing number

        expSum = 0  # Expected sum of numbers from 1 to n^2
        actualSum = 0  # Sum of all numbers present in the grid
        s = set()  # Set to track seen numbers

        # Iterate through each element of the 2D grid
        for i in range(n):
            for j in range(n):
                actualSum += grid[i][j]  # Add current number to actual sum

                if grid[i][j] in s:  # If number is already in set, it's repeated
                    a = grid[i][j]  # Store repeated number
                    ans.append(a)  # Add repeated number to answer list
                s.add(grid[i][j])  # Add number to the set

        # Calculate expected sum of numbers from 1 to n^2
        expSum = (n * n) * (n * n + 1) // 2

        # Derive the missing number using formula: missing = expected_sum + repeated - actual_sum
        b = expSum + a - actualSum
        ans.append(b)  # Add missing number to answer list

        return ans  # Return the answer [repeated, missing]


# ----------- Input and Output -----------

# Take input for grid size
n = int(input("Enter the size of the grid (n for n x n): "))

# Initialize empty grid
grid = []

# Take input for each row
print(f"Enter the {n}x{n} grid rows (space-separated numbers):")
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Create instance of Solution
solution = Solution()

# Call the method
result = solution.findMissingAndRepeatedValues(grid)

# Print the result
print("Repeated and Missing numbers:", result)


"""
Example Input:
Enter the size of the grid (n for n x n): 2
Enter the 2x2 grid rows (space-separated numbers):
1 2
2 3
Repeated and Missing numbers: [2, 4]
"""
