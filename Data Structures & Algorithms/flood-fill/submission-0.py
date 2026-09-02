class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        bools = []
        for i in range(len(image)):
            bools.append([])
            for j in range(len(image[i])):
                bools[i].append(False)
        self.floodFillRecursive(image,sr,sc,image[sr][sc],bools,color)
        return image
    def floodFillRecursive(self,image,sr,sc,color,marked,target_color):
        if marked[sr][sc]:
            return
        if image[sr][sc] != color:
            return
        image[sr][sc] = target_color
        marked[sr][sc] = True
        if self.inArr(image,sr-1,sc):
            self.floodFillRecursive(image,sr - 1 , sc,color,marked,target_color)
        if self.inArr(image,sr+1,sc):
            self.floodFillRecursive(image,sr+1 , sc,color,marked,target_color)
        if self.inArr(image,sr,sc-1):
            self.floodFillRecursive(image,sr , sc-1,color,marked,target_color)
        if self.inArr(image,sr,sc+1):
            self.floodFillRecursive(image,sr , sc+1,color,marked,target_color)
    def inArr(self,image,sr,sc):
        return sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0])
