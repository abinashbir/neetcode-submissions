class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0

        for _ in details:
            if int(_[11:13]) > 60:
                count+=1
        return count    