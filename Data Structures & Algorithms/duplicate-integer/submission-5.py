class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dup=list(set(nums))


        if len(non_dup) != len(nums):
            return True
        else :
            return False
        