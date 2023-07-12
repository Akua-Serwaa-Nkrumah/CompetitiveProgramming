#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            if current_sum < target:
                left+=1
            if current_sum > target:
                right-=1
        return []
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
