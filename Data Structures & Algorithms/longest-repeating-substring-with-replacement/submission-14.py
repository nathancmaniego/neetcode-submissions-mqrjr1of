class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        aabcd, k = 2
        a: 2, b: 1, c: 1
         < 4
        a: 1, b: 1, c:1
         1 + 2 = 3, end - start = 4
        b: 1, c:1 < 1 + 2
        b
        XYYX

        [AAB]A
        [AAB]A 
        [AAB] > MAX_FREQ + 0
        [AAB] > 2 + 0
        [AB] > 1
        [B] > 1
        
        
        {a: 2, b:1}
        
        """
        l = 0
        count = {}
        res = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(count[s[r]], maxf)
            while ((r - l + 1) - maxf > k):
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
