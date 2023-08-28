class Solution:
    # # Python rocks! But this is not a good answer :-)
    # def reverseString(self, s: List[str]) -> None:
    #     s.reverse()
    #
    # # Or this....
    # def reverseString(self, s: List[str]) -> None:
    #     s[:] = s[::-1]

    # # Iterative approach:
    # # None, [] => does nothing
    # # ['a','b']
    # # ['x','y','z']
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     if not s:
    #         return
    #     tmp = None
    #     begin = 0
    #     end = len(s) - 1
    #     while begin < end:
    #         tmp = s[begin]
    #         s[begin] = s[end]
    #         s[end] = tmp
    #         begin += 1
    #         end -= 1
    
    # # NOTICE WE DO NOT NOT NOT NOT NOT NOT NOT NOT NOT NOT NEED TO USE TMP AT ALL!!!!
    # def reverseString(self, s):
    #     left, right = 0, len(s) - 1
    #     while left < right:
    #         s[left], s[right] = s[right], s[left]  # <= !!!!!!!!
    #         left, right = left + 1, right - 1
    
    # Solved again on 5/30/23
    def reverseString(self, s: List[str]) -> None:
        # # Because 1 <= s.length <= 105, I do not need to check for empty string
        # l = 0
        # r = len(s) - 1
        # while (l < r):
        #     l_str = s[l]
        #     s[l] = s[r]
        #     s[r] = l_str
        #     l += 1
        #     r -= 1
        # return s
        # This is clearer....
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
    
    
    # # Recursive 
    # def reverseString(self, s):
    #     def helper(s, begin, end):
    #         if begin >= end:
    #             return
    #         s[begin], s[end] = s[end], s[begin]        
    #         helper(s, begin + 1, end - 1)
    #     helper(s, 0, len(s) - 1)
    
    
    
    # # WRONG approach:
    # def reverseString(self, s: List[str]) -> None:
    #     if not s:
    #         return
    #     return self.reverseString(s[1:]) + [s[0]]
    # # Example: ['a','b','c']
    # # r(['a','b','c']) => r(['b','c']) + ['a'] => r(['c']) + ['b'] => r([]) + ['c'] => return
