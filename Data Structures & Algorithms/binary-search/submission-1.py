class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while nums[mid] != target and start < end:
            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        else:
            return -1

