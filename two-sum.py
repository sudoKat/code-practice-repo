'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices i and j such 
that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy 
the condition.
Return the answer with the smaller index first.

'''
def twoSum(self, nums: list[int], target: int) -> list[int]:
       
       'Hashmap in Python is Dictionary' 
       nums_dict = {}

       for i in range(len(nums)):
        diff = target - nums[i]

        'Check if the difference already exists in the dictionary'
        if (((diff) in nums_dict) and (i != nums_dict[diff])):

            'The smaller index needs to be returned first'
            if (i < nums_dict[diff]):
                return [i, nums_dict[diff]]
            else:
                return [nums_dict[diff], i]
            
        'Appending a new key, so that for [5,5], the code gets no error'
        nums_dict[nums[i]] = i

        return []

