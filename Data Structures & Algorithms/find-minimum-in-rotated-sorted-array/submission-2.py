class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:


            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            m = (left + right) // 2
            print("left:" + str((nums[left], left)))
            print("right:" + str((nums[right], right)))
            print("mid:" + str((nums[m], m)))
            
            res = min(res, nums[m])
            if nums[m] >= nums[left]:
                print(" left inc")
                left = m + 1
            else:
                print(" right dec")

                right = m - 1
        return res