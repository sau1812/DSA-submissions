class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        logest = 0

        for i in nums:
            if (i - 1) not in numset:
                L = 0
                while (i + L ) in numset:
                    L += 1
                logest = max(logest, L)
        return logest
        