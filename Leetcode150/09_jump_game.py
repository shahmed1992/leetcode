"""

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


"""

def can_jump(nums):
    # [2,3,1,1,4]. [3,2,1,0,4]
    # idx = 0
    # distance_covering = []
    # for i in range(len(nums)):
    #     distance_covering[i]+=
    # while idx!=len(nums)-1:
    #     if nums[idx]==0:
    #         return False

    goal = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        # print(i)
        if nums[i]>=(goal-i):
            goal = i
    if goal == 0:
        return True
    else:
        return False

inputs = [[2,3,1,1,4], [3,2,1,0,4] ]
for inpt in inputs:
    res = can_jump(inpt)
    print(f"For Input:{inpt}: {res}")
