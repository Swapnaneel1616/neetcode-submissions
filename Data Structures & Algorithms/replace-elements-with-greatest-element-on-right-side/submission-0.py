class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        r = n-1
        maxx = arr[n-1]
        for i in range(n-2 , -1 , -1):
            if(arr[i]< maxx):
                arr[i] = maxx
            else:
                new_max = arr[i]
                arr[i] = maxx
                maxx = new_max
        arr[n-1] = -1

        return arr