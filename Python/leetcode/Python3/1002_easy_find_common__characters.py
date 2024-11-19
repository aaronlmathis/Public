class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res = []

        common_count = {}
        
        for letter in words[0]:
            common_count[letter] = common_count.get(letter, 0) + 1

        for word in words[1:]:
            current_count = {}
            for letter in word:
                current_count[letter] = current_count.get(letter, 0) + 1

            for letter in common_count:
                if letter in current_count:
                    common_count[letter] = min(common_count[letter], current_count[letter])
                else:
                    common_count[letter] = 0

        for letter, count in common_count.items():
            res.extend([letter] * count)

        return res

words = ["bella","label","roller"]
sol = Solution()
print(sol.commonChars(words))