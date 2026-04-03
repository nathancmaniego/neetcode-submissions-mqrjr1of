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
        start = 0
        max_count = 1
        seen = {}
        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end], 0) + 1
            max_freq = max(seen.values())
            if max_freq + k > end - start:
                max_count = max(max_count, end - start + 1)
                print(s[start:end + 1]+ str(max_count))
            else:
                print(end - start + 1)
                print(max_freq + k)
                while end - start + 1 > max_freq + k:
                    print("entered")
                    seen[s[start]] -= 1
                    start += 1
                    
                max_count = max(max_count, end - start)
                print("new" + s[start:end + 1] + str(max_count))

        return max_count