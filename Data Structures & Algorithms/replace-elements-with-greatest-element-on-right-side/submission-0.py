class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            num = arr[i]
            arr[i] = maxNum
            if num > maxNum:
                maxNum = num
        return arr