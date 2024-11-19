class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        
        d = {}
        for k,v in enumerate(names):
            d[v] = heights[k]
        so = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res = [v for k,v in enumerate(so)]
        return res
        """
        # Zip names and heights together and sort by height in descending order
        sorted_people = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        
        # Extract the names from the sorted list of tuples
        res = [name for name, height in sorted_people]
        
        return res    

names = ["Mary","John","Emma"] 
heights = [180,165,170]
sol = Solution()
print(sol.sortPeople(names, heights))