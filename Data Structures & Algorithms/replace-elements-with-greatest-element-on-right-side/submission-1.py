class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        right = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = right
            right = max(arr[i],right)
        return ans

        