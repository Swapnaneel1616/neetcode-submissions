class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}

        for i , num in enumerate(nums):
            diff = target - num
            if diff in mpp:
                return [mpp[diff] , i]
            else:
                mpp[num] = i

        return []  