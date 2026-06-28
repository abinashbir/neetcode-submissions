class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[c for c in s]
        t_list=[c for c in t]
        s_list.sort()
        t_list.sort()
        if len(s_list) != len(t_list) :
            return False
        elif s_list == t_list:
            return True
        else:
            return False
            

        