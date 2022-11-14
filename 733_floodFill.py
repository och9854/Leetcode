class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # get current value
        curr = image[sr][sc]
        R = len(image)
        C = len(image[0])
        
        
        '''wrong
        # up 
        if  ( sr-1 >= 0) and (image[sr-1][sc] == curr) :
            image[sr-1][sc] = color
            return self.floodFill(image, sr-1, sc, color)
        # down 
        if ( sr+1 < m ) and (image[sr+1][sc] == curr)  :
            image[sr+1][sc] = color
            return self.floodFill(image, sr+1, sc, color)
        
        # left
        if  ( sc-1 >= 0) and (image[sr][sc-1] == curr) :
            image[sr][sc-1] = color
            return self.floodFill(image, sr, sc-1, color)
        
        # right
        if  ( sc+1 < n) and (image[sr][sc+1] == curr) :
            image[sr][sc+1] = color
            return self.floodFill(image, sr, sc+1, color)
        '''
        
        '''answer'''
        if color == curr:
            return image
        
        def dfs(r,c):
            if image[r][c] == curr:
                image[r][c] = color
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
             
        dfs(sr,sc)         
                
        return image  
        
        
        

# feedback
'''
- does not have to learn only with a function -> use inner loop!
- just code outside of inner function which need only one operation during execution
- put others in it
'''