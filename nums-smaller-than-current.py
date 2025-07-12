'''
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array 
are smaller than it. That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        dict_nums = {}
       
        'Sort the list first'
        nums_sorted = sorted(nums)
       
        'Loop through the sorted list, saving the index as key. This key tells us how many numbers are smaller than the current number.'
        for i,num in enumerate(nums_sorted):
            if num not in dict_nums:
                dict_nums[num] = i
       
        'Create solution list, assigning the "key" value in from the dictionary for each value in nums.'
        ret = []
        for i in nums:
            ret.append(dict_nums[i])

        return ret