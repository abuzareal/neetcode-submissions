class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)
                    
        return False
        