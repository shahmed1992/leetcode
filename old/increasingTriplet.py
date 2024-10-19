class Solution:
    def increasingTriplet(self, nums ):
        # Approach-1 => Failed
        # count = 0
        # for i in range(len(nums)-2):
        #     for j in range(1,len(nums)-1):
        #         for k in range(2,len(nums)):
        #             if nums[i]<nums[j]<nums[k] and i<j<k:
        #                 print("indices",i,j,k)
        #                 count+=1
        #                 # return True
        # return False
        # i = 0
        # j = 1
        # for k in range(2,len(nums)):
        #     if nums[k]<nums[i]:
        #         i = k
        #         j = i+1
        #     elif nums[k]<nums[j] and nums[k] > nums[i]:
        #         j = k
        #     else:
        #         return True

        # return False
        # SOlution -2 => Failed
        # i = 0
        # j = 1
        # k = 2
        # while k <len(nums):
        #     print(i,j,k)
        #     if nums[k]<=nums[i]:
        #         i = j
        #         j = i+1
        #         k = j+1
        #     elif nums[k]<=nums[j] and nums[k]>nums[i]:
        #         j = k
        #         k+=1
        #     else:
        #         return True
        # return False

        # Solution - 3 => Success

        num_i=num_j=float('inf')
        for num in nums:
            if num<=num_i:
                num_i = num
            elif num<=num_j:
                num_j=num
            else:
                return True
        return False

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
list3 = [2,1,5,0,4,6]
list4 = [0,4,2,1,0,-1,-3]
list5 = [20,100,10,12,5,13]
list6 = [1,2,2,1]
list7 = [5,1,6]
solution = Solution()
print(solution.increasingTriplet(list1)) #True
print(solution.increasingTriplet(list2)) #False
print(solution.increasingTriplet(list3)) #True
print(solution.increasingTriplet(list4)) #False
print(solution.increasingTriplet(list5)) #True
print(solution.increasingTriplet(list6)) #False
print(solution.increasingTriplet(list7)) #False
'''
Testing Inputs:
    [1,2,3,4,5]
    [5,4,3,2,1]
    [2,1,5,0,4,6]
'''
