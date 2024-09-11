class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        l = [numeral_values[char] for char in s]
        total = 0
        for i in range(len(l)):
            if i == len(l) - 1: #last iteration
                current = l[i]
                return total + current
            else:
                current = l[i]
                next = l[i+1]
                if current < next: # If current value is less than value to the right, subtract it from value on right and add to overall sum
                    total -= current
                else: # If number to the right is equal, add the two together and add to total
                    total += current

        






sol = Solution()
foo = sol.romanToInt("III")
print(foo)