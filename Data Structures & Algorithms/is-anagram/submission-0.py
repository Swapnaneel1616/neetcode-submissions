class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for char in range(len(s)):
            s_key = s[char]
            if s_key in map1:
                map1[s_key] += 1
            else:
                map1[s_key] = 1

        for char in range(len(t)):
            t_key = t[char]
            if t_key in map2:
                map2[t_key] += 1
            else:
                map2[t_key] = 1

        return map1 == map2
        
