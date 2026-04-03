class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]