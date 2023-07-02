class Solution:
    def dfs(self, node, isVisited, edgeMap):
        if isVisited[node]:
            return isVisited
        
        isVisited[node] = True
        for adjcentNode in edgeMap[node]:
            self.dfs(adjcentNode, isVisited, edgeMap)
        return isVisited

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # edgeMapの構築
        edgeMap = defaultdict(list)
        for edge in edges:
            edgeMap[edge[0]].append(edge[1])
            edgeMap[edge[1]].append(edge[0])
        
        # 探索
        counter = 0
        isVisited = [False for _ in range(n)]
        for i in range(n):
            if isVisited[i]:
                continue
            
            isVisited = self.dfs(i, isVisited, edgeMap)
            counter += 1
        return counter
        
