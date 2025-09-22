"""
Given an integer array nums, write a function sort_by_parity() that moves all the even integers to the beginning of the array, followed by all the odd integers.
nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)

[2, 4, 3, 1]
[0]
"""

def sort_by_parity(nums):
    result = []

    if not nums:
        print([])

    for num in nums:
        if num % 2 == 0:
            result.append(num)
    for num in nums:
        if num % 2 != 0:
            result.append(num)

    print(result)


nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)