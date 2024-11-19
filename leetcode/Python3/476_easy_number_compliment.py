class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
       
        res = []
        while num > 0:
            r = num % 2
            res.append(r)
            num = num // 2

        res.reverse()
        com = ''
        for n in res:
            if n == 0:
                com+= '1'
            else:
                com+='0'

        return int(com, 2)
         """
        # Convert the number to binary, strip off the '0b' prefix, and flip the bits
        binary_str = bin(num)[2:]
        
        # Generate the complement by flipping each bit
        complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        
        # Convert the complement binary string back to an integer
        return int(complement_str, 2)
        
sol = Solution()
num = 5
print(sol.findComplement(num))