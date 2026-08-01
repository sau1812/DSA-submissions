class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            count[i] = count.get(i , 0) + 1
        for v in count.values():
            if v > 1:
                return True
        return False