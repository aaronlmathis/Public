class Solution:
    def hIndex(self, citations: list[int]) -> int:
        possible = []
        for c in citations:
            count = 0
            for i in range(len(citations)):
                if citations[i] >= c:
                    count+=1
            if count >= c:
                possible.append(c)
            else:
                possible.append(count)
        if not possible:
            return len(citations)
        else:
            return max(possible)


sol = Solution()
nums = [0,0,4,4]
print(sol.hIndex(nums))