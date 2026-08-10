class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        check1 = [0]*26
        check2 = [0]*26
        if n1 > n2:
            return False
        for i in range(n1):
            check1[ord(s1[i]) - ord('a')] += 1
            check2[ord(s2[i]) - ord('a')] += 1
        if check1 == check2:
            return True
        for i in range(n1, n2):
            check2[ord(s2[i]) - ord('a')] += 1
            check2[ord(s2[i - n1]) - ord('a')] -= 1

            if check1 == check2:
                return True
        return False


