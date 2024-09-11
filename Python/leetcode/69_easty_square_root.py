class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        try:
            while left <= right:
                mid = left + (right - left) // 2
                m = mid * mid
                if m == x:
                    return mid
                elif m < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        except TypeError as e:
            print(f"Error: {e}")  # This prints the default error message associated with the exception
            print(f"Detailed Error: The provided value '{x}' is not a valid integer.")
            return None
        
            
                

sol = Solution()
print(sol.mySqrt('c'))