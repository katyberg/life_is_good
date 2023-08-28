class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # i is index into s, j is index into t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
                # if s[i] == t[j]:
                #     i += 1
                #     j += 1
                # else:
                #     j += 1
        if i == len(s):
            return True
        return False

   
# s = ""
# t = ""

# s = "axc"
#       i
# t = "ahbgdc"
#            j
