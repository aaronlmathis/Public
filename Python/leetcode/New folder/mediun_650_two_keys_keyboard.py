class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def prime_factors(n):
            factors = []
            
            # Divide n by 2 until it becomes odd
            while n % 2 == 0:
                factors.append(2)
                n //= 2
            
            # Now n must be odd, so we can skip even numbers
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors.append(i)
                    n //= i
            
            # If n is still a prime number greater than 2
            if n > 2:
                factors.append(n)
            
            return factors
        
        factors = prime_factors(n)
        res = 0
        for num in factors:
            res += num

        return res
        
n = 1
sol = Solution()
print(sol.minSteps(n))