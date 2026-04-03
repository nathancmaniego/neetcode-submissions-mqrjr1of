class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # [1,2,4,6]
        # PRE: [1,1,2,8]
        # SUF: [48,24,6,1]
        prefix = n * [0]
        suffix = n * [0]
        result = n * [0]
        prefix[0] = 1
        suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        print(prefix)
        print(suffix)
        return result