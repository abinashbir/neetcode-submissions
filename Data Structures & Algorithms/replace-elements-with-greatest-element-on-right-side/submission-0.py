class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        ans = [0] * len(arr)
        for i in range(len(arr)):
            right = -1
            for j in range(i+1,len(arr)):
                    right = max(right,arr[j])
            ans[i] = right
        return ans
            

        