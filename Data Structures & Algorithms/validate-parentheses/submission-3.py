class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        e = {')': '(',
             '}': '{',
             ']': '['}
        if s == "":
            return True
        for c in s:
            if c not in e:
                lst.append(c)
            if c in e:
                if len(lst) != 0 and lst.pop() == e[c]:
                    continue
                else:
                    return False
            print(lst)
            
        return len(lst) == 0