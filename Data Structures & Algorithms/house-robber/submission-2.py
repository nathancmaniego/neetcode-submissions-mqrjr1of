class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0 # i is out of bounds
            if memo[i] != -1:
                return memo[i] # i is already computed
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)