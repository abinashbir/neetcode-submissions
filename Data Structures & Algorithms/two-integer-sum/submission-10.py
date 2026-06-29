class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first,second=0,0
        for i in range(len(nums)):
            first=nums[i]
            for j in range(len(nums)-1,-1,-1):
                second=nums[j]
                if i!=j and first+second==target:
                    return [i,j]
            