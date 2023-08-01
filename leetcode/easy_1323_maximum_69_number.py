class Solution:
    def maximum69Number (self, num: int) -> int:
        # Intuition:
        # find the first 6 if exist and change it to 9
        new_num = ''
        num_modified = 0
        for c in str(num):
            if c == '6' and num_modified < 1:  # turn first 6 into 9 (at most once)
                new_num += '9'
                num_modified += 1
            else:
                new_num += c
        return int(new_num)

        # # Or use built-in function
        # num_string = str(num)
        # return int(num_string.replace('6', '9', 1))

