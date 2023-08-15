# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permutations(arr):
    print(arr)
    
    
    
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
  
            # if all integers are used up
            if first == n:  
                output.append(nums[:])

            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                #print(nums[i], nums[first])
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output
    
arr = [1,2,3,3,5]    
sol = Solution()
print(sol.permute(arr), len(sol.permute(arr)))    
