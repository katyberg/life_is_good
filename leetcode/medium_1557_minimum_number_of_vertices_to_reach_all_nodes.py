class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # KEY of this problem is to find => all nodes with IN-DEGREE=0!!!!
        # Once we identify that, this problem becomes SUPER simple!!!!
        indegree = [0] * n
        # edge [x, y] means there is 1 indegree for y.
        for x, y in edges:
            indegree[y] += 1
        return [i for i, num in enumerate(indegree) if num == 0]
