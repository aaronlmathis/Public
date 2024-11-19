class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        words = {}
        prefix = ""
        for k, v in enumerate(strs):
            letters = [char for char in v]
            words[k] = letters 
        
        #find the shortest list in dictionary
        curr_length = 0
       
        for k, v in words.items():
            if curr_length == 0:
                curr_length = len(v) 
            else:
                if curr_length > len(v):
                    curr_length = len(v)


        #loop through the the lists as many times as the shortest length.
        for i in range(curr_length):
            items = []

            for k, v in words.items():
                items.append(v[i])    
                   
            all_equal = all(item == items[0] for item in items)
            if(all_equal):
                prefix = prefix + items[0]


        return prefix


lists = ['flower', 'flour', 'flub', 'flub']
sol = Solution()
value = sol.longestCommonPrefix(lists)
print(value)