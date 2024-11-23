"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


"""

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # print(nums, end=" ")

    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

print(rotate([x for x in range(1,8)], 3))
print(rotate([ -1, -100, 3, 99], 2))