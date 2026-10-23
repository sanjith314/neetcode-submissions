class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ","")
        start=0
        end=len(st)-1
        while(start<end):
            if not st[start].isalnum():
                start += 1
                continue
            if not st[end].isalnum():
                end -= 1
                continue
            if(st[start].lower() != st[end].lower()):
                return False
            start+=1
            end-=1
        return True