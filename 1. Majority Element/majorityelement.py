def majorityElement(nums):
    frequency = 0
    answer = nums[0]

    for num in nums:
        if frequency == 0:
            answer = num
        if num == answer:
            frequency += 1
        else:
            frequency -= 1
    return answer


# ---- Take input from the user ----
# Example input: 2 2 1 1 1 2 2
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Find and print the result
result = majorityElement(nums)
print("Majority element is:", result)
