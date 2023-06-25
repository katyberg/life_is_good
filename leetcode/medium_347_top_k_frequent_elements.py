from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # Counter for n
        # {
        #   1: 2,
        #   2: 5,
        #   3: 1,
        #   4: 5
        # }
        # sort by counts
        count_num = []
        for num, count in counter.items():
            count_num.append((count, num))
        # IMPORTANT! when sorting tuples we need to specify the sort key if order matter!
        # Ex: [(5, 4), (5, 2), (2, 1), (1, 3)]
        count_num.sort(key=lambda t: t[0], reverse=True)
        result = []
        for i in range(k):
            result.append(count_num[i][1])
        return result

        # NOTE THAT THIS FUNCTION COULD BE A ONE-LINER!!!!
        # DUH!!!!
        # return list(map(lambda x: x[0], Counter(nums).most_common(k)))
        # return [key for key, _ in Counter(nums).most_common(k)]


def test() -> None:
    nums = [1,4,2,2,1,4,2,3,4,2,2,4,4]
    s = Solution()
    output = s.topKFrequent(nums, 3)
    expected_output = [4,2,1] or [2,4,1]
    assert output == expected_output
    print(f'output={output}')


if __name__ == "__main__":
    test()
