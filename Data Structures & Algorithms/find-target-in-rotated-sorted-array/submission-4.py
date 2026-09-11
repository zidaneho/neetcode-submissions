class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            #sorting rotation divider must happen in the block
            if nums[mid] > nums[right]:
                if target <= nums[right] or target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            #block is perfectly sorted
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid
        if nums[left] == target:
            return left
        return -1