class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True
        
        if len(s) == 1 and len(t) == 1:
            return s[0] == t[0]


        while j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == len(s):
                return True
        return False


