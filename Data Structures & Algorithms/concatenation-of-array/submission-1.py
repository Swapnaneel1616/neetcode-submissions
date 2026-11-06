class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #Append
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums
            