'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums, target) :
        
        # Approach-1
        # for i in range(len(nums)-1):
        #     if nums[i]+nums[i+1]==target:
        #         return (i,i+1)
        # return -1
    
        # Approch-2
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum([2,7,11,15],9)
    print(res)
