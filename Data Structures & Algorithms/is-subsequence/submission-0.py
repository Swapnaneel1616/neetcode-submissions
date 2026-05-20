class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        j= 0

        for i in range(len(t)):
            if(j< len(s)):
                if(s[j] == t[i]):
                    j+=1
                
        return len(s) == j