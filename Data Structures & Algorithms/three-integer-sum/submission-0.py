class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(0, n-2):
            j = i+1
            k = n-1

            while j < k:
                calc = nums[i] + nums[j] + nums[k]

                if calc == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j+= 1
                    k-= 1
                
                elif calc < 0:
                    j += 1
                
                else:
                    k -= 1
        
        return res