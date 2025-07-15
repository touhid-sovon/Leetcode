class NumMatrix:

    def __init__(self,matrix:list[list[int]]):
        Row,Col = len(matrix),len(matrix[0])

        # adding extra padding for edge cases
        self.matSum = [[0]*(Col+1) for _ in range(Row+1)]

        for r in range(Row):
            prefix = 0
            for c in range(Col):
                prefix += matrix[r][c]
                above = self.matSum[r][c+1]
                self.matSum[r+1][c+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1

        bottomLeft = self.matSum[row2][col2]
        above = self.matSum[row1-1][col2]
        left = self.matSum[row2][col1-1]
        top_left = self.matSum[row1-1][col1-1]

        return bottomLeft - above - left + top_left
