class Solution:
    def arrangeCoins(self, n: int) -> int:
        # row = 0
        # while n - row > 0:
        #     row += 1
        #     n -= row
        # return row
        #Brute Force

        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) // 2
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)

        return res