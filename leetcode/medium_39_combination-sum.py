class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # curr: the current array
        # pos: current index in the candidates list
        # curr_sum: the sum of all elements in current array
        # (don't need this but add it for performance reason)
        def backtrack(curr, pos, curr_sum):
            # print(f'curr={curr}, pos={pos}, curr_sum={curr_sum}')
            # we have two base bases:
            if curr_sum == target:
                answer.append(curr[:])
                return
            elif curr_sum > target:
                return
            for i in range(pos, len(candidates)):
                curr.append(candidates[i])
                curr_sum += candidates[i]
                # backtrack(curr, pos, curr_sum)  # this is where I got stuck in first pass!
                backtrack(curr, i, curr_sum)
                # IMPORTANT!!!! REMEMBER TO REMOVE CURRENT CHARACTER FROM SUM!!!!
                # I FORGOT THE FIRST TIME AROUND!!!!
                curr.pop()
                curr_sum -= candidates[i]

        answer = []
        backtrack([], 0, 0)
        return answer

