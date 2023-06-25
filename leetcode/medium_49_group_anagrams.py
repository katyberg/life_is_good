class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Below solution does NOT work!!!! Example below.
        # # Input:
        # # strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
        # # Output = [["cab"],["tin"],["pew"],["duh","ill"],
        # #.          ["may"],["buy"],["bar"],["max"],["doc"]]
        # # Expected : [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],
        # #             ["bar"],["pew"],["cab"]]
        # # ^^^^ Note that both "duh" and "ill" generates same hash 132!!!!
        # # THIS IS WRONG BECAUSE ord('d')+ord('u')+ord('h') == ord('i')+ord('l')+ord('l')
        # def _hash(string: str):
        #     sum = 0
        #     for char in string:
        #         sum += ord(char)  # convert to ASCII; it is int type
        #     return sum
        # groups = defaultdict(list)  # defaultdict(List[str]) is WRONG!
        # for string in strs:
        #     key = _hash(string)
        #     # print(f'string={string}')
        #     # print(f'key={key}')
        #     groups[key].append(string)
        # result = []
        # for k, v in groups.items():
        #     result.append(v)
        # if not groups:
        #     result.append([])
        # return result

        groups = defaultdict(list)  # defaultdict(List[str]) is WRONG!
        for string in strs:
            key = ''.join(sorted(string))
            groups[key].append(string)
        # Just return the values, note that [''] and [] are not the same....
        return list(groups.values())

        # result = []
        # for k, v in groups.items():
        #     result.append(v)
        # if not groups:
        #     result.append([])
        # return result

