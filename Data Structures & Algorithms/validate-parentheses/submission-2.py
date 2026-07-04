class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for c in s:
            if c == "(" or c == "{" or c== "[":
                a.append(c)
            else:
                if not a:
                    return False
                top = a.pop()
                if c == ')' and top!='(':
                    return False
                if c == '}' and top!='{':
                    return False
                if c == ']' and top!='[':
                    return False
        return len(a) == 0