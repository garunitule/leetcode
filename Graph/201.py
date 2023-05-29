class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(i, j):
            passed[i][j] = True
            if grid[i][j] == "0":
                return

            if j+1 < n and passed[i][j+1] == False:
                explore(i, j+1)
            
            if -1 < j-1 and passed[i][j-1] == False:
                explore(i, j-1)
            
            if -1 < i-1 and passed[i-1][j] == False:
                explore(i-1, j)
            
            if i+1 < m and passed[i+1][j] == False:
                explore(i+1, j)


        m = len(grid)
        n = len(grid[0])
        passed = [[False for _ in range(n)] for _ in range(m)]

        answer = 0
        for i in range(m):
            for j in range(n):
                # 訪れた場合は何もしない
                if passed[i][j] == True:
                    continue

                # まだ訪れてないlandなら、island判定する
                if grid[i][j] == "1":
                    answer += 1

                    # 隣接したlandを訪れる
                    explore(i, j)
        return answer
