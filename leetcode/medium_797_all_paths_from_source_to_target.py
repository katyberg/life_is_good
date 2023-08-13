class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Intuition:
        # path exploration in a graph data structure -> think "backtracking"!
        # Build the RECURSIVE TREE first!!!!
        # Backtracking has "exponential time" => O(2^N * N) => 2^N recursive calls, each runs N times.
        def backtrack(curr, i):
            if i == end:
                answer.append(curr[:])
                return
            connections = graph[i]
            for connection in connections:
                curr.append(connection)
                backtrack(curr, connection)
                curr.pop()
        begin = 0
        end = len(graph) - 1  # 2 <= n <= 15
        answer = []
        backtrack([begin], begin)
        return answer
                
