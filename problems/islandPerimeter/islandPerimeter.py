class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    adder = 4
                    if j > 0:
                        if grid[i][j-1] == 1:
                            adder -= 1 
                    if i < len(grid)-1:
                        if grid[i-1][j] == 1:
                            adder -= 1 
                    if j < len(grid[i]):
                        if grid[i][j+1] == 1:
                            adder -= 1
                    if i < len(grid)-1:
                        if grid[i+1][j] == 1:
                            adder -= 1 
                    sum += adder
        return(sum)