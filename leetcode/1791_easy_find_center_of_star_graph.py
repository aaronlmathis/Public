class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        collection = {}
        for edge in edges:
            for line in edge:
                if line in collection:
                    collection[line] += 1
                else:
                    collection[line] = 1
        
        return max(collection, key=collection.get)


edges = [[1,2],[5,1],[1,3],[1,4]]
sol = Solution()
print(sol.findCenter(edges))        