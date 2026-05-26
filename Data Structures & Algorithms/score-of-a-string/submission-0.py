class Solution:
    def scoreOfString(self, s: str) -> int:
        j = 0
        count = 0
        for i in range(1, len(s)):
            count += abs(ord(s[i]) - ord(s[j]))
            j+=1

        return count 