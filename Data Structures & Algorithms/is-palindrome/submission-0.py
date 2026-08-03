class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl = [ch.lower() for ch in s if ch.isalnum()]
        l,r = 0,len(cl)-1
        while l<r:
            if cl[l] != cl[r]:
                return False
            l += 1
            r -= 1
        return True
        