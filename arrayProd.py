import math
class Solution:
    def productExceptSelf(self, nums ):
        '''res = []
        key = 0
        for i in range(len(nums)):

            # res.append(math.prod(nums)//nums[i])
        print(res)
        '''
        '''
        1. have a list for prefix product
        2. hava a list for suffix product
        3. create 
        '''
        prefixProduct=[0]*len(nums)
        prefixProduct[0] = 1
        suffixProduct = [0]*len(nums)
        suffixProduct[-1] = 1
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            prefixProduct[i] = nums[i-1]*prefixProduct[i-1]


        for i in range(len(nums)-2,-1,-1):
            suffixProduct[i] = nums[i+1]*suffixProduct[i+1]


        # calculating the resultant array
        for i in range(len(nums)):
            res[i]=prefixProduct[i]*suffixProduct[i]


solution = Solution()
solution.productExceptSelf([1,2,3,4])

"""
    1. First find out prefix product of all elements
    2. Find out suffix product of all elements in the list
    3. Last step is calculating resultant list, where res[i] = prefix[i]*suffix[i]
    
    1. To find prefix product:
        a. [1,2,3,4] => [1,2,6,24]
    2. Suffix product:
        a. [1,2,3,4] => [24,24,12,4] 
    3. Resultant list:
        a. [1,2,3,4] => [24, 12, 8,6]
"""
