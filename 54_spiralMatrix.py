#JK
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0]) # eg. 3,3
        up = left = 0
        right = columns - 1 # 2
        down = rows - 1 # 2

        while len(result) < rows * columns:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downsize
            for row in range(up+1, down+1):
                result.append(matrix[row][right])

            # check if it's not in the different row
            if up!= down:
                # right -> left
                for col in range(right-1, left, -1):
                    result.append(matrix[down][col])

            # check if it's not in the different col
            if left != right:
                for row in range(down, up, -1 ):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1
        return result

        
            
