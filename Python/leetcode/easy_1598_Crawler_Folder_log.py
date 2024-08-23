class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count = 0
        for item in logs:
            print (item[0])
            if item[0] == '.':
                if item[1] == '.':
                    if count >= 1:
                        count-=1
            else:
                count+=1

        return count if count > 0 else 0     


sol = Solution()
logs = ["d1/","d2/","./","d3/","../","d31/"]
print(sol.minOperations(logs))