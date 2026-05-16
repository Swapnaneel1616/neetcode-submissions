class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) -1 
        left = 0
        final_arr = []
        while(left<right):
            sum = numbers[right] + numbers[left]
            if (sum == target):
                final_arr.append(left+1)
                final_arr.append(right+1)
                return final_arr

            elif (sum<target):
                left += 1

            else:

                right -=1

        return final_arr