class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        passed = [[False for _ in range(n)] for _ in range(m)]
        max_area = 0

        def traverse(i, j):
            # 上下左右に隣接するlandを探索するので、前に通ったlandを再度探索する可能性がある
            # そのため、一度通ったlandを避ける必要がある
            if passed[i][j]:
                return 0
            passed[i][j] = True
        
            area = 1
            if -1 < i-1 and grid[i-1][j] == 1:
                area += traverse(i-1, j)
            
            if i+1 < m and grid[i+1][j] == 1:
                area += traverse(i+1, j)
            
            if -1 < j-1 and grid[i][j-1] == 1:
                area += traverse(i, j-1)
            
            if j+1 < n and grid[i][j+1] == 1:
                area += traverse(i, j+1)
            
            return area


        for i in range(m):
            for j in range(n):
                # すでに通った場所は無視
                if passed[i][j]:
                    continue
                
                # 通ってないlandが所属するareaを計算する
                if grid[i][j] == 1:
                    max_area = max(traverse(i, j), max_area)
        return max_area


