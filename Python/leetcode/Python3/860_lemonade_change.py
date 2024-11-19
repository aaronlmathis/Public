class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0  # Initialize counters for $5 and $10 bills
        
        for pay in bills:
            if pay == 5:
                five += 1  # If the customer pays with $5, no change is needed
            elif pay == 10:
                if five == 0:
                    return False  # Can't give $5 as change
                five -= 1  # Give one $5 as change
                ten += 1  # Collect the $10 bill
            elif pay == 20:
                if ten > 0 and five > 0:
                    ten -= 1  # Give one $10
                    five -= 1  # Give one $5
                elif five >= 3:
                    five -= 3  # Give three $5 bills as change
                else:
                    return False  # Can't give correct change
            print(f"Current state - $5 bills: {five}, $10 bills: {ten}")
        
        return True  # If we can give correct change for all customers

sol = Solution()
bills = [5,5,10,10,20]
print(sol.lemonadeChange(bills))

