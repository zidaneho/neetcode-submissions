class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        for i in range(2,n):
            arr[i] = arr[i-2] + arr[i-1]
        print(arr)
       
        return arr[n-1]

   
