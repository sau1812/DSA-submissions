class Solution:
    def twoSum(self, nums, target):
        count = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in count:
                return [count[diff], i]
            count[n] = i

        return
        