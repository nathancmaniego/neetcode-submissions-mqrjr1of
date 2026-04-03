class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = defaultdict(int)
        
        max_count = 0
        for n in nums:
            if not check[n]:
                check[n] = check[n - 1] + check[n + 1] + 1
                check[n - check[n-1]] = check[n]
                check[n + check[n+ 1]] = check[n]
                max_count = max(max_count, check[n])
        return max_count
            