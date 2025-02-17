"""
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. 

You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Example:
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
Output
[null,null,null,null,null,null,20,40,0,null,32]
Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 
Constraints:
0 <= nul <= 100
1 <= k <= 4 * 104
At most 4 * 104 calls will be made to add and getProduct.
The product of the stream at any point in time will fit in a 32-bit integer.
 

Follow-up: Can you implement both GetProduct and Add to work in O(1) time complexity instead of O(k) time complexity?
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

class ProductOfNumbers:

    def __init__(self):
        self.__stream = [1]                 # Create read-only list and initialize it with 1 for proper multiplication.
        self.__product = [1]                # `product` holds the product of all numbers up to an index
        self.__zero = False                 # Initialize `zero` as boolean flag indicating last number was a 0.
        self.__most_recent_zero = None      # Track most recent instance of `0` added.
    
    def add(self, num: int) -> None:
        # Check if last number added to stream was `0`
        # If it was, then we want to start the product totals over at `num`
        # Otherwise, append `num` * `__product[-1]`
        if self.__zero:                     
            self.__product.append(num)
            self.__zero = False
        else:
            self.__product.append(num * self.__product[-1])
        # If the current `num` is zero, mark `__zero` True and set `__most_recent_zero` to current index of `__stream`
        if num == 0:
            self.__most_recent_zero = len(self.__stream)
            self.__zero = True
        self.__stream.append(num)
    @timed
    def getProduct(self, k: int) -> int:
        # If the index of the item in `__stream` before `k` values is < the index of most recent zero, return 0 because `k` numbers has a zero in it.
        if self.__most_recent_zero is not None and (len(self.__stream) -k -1) < self.__most_recent_zero:
            return 0
        # If the index of the item in `__stream` before `k` values is equal to the index of most recent zero, just return the running product total.
        elif self.__most_recent_zero is not None and (len(self.__stream) -k -1) == self.__most_recent_zero:
            return self.__product[-1]
        
        # If the index of the item in `__stream` before `k` values is > than the index of the most recent zero (or there are no zeros) 
        # return the total product divided by the product of the item before index `k`
        return self.__product[-1] // self.__product[- k - 1]


[1,5,3,6,7]
[1,1,5,15,90]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)        # [3]
productOfNumbers.add(0)        # [3,0]
productOfNumbers.add(2)        # [3,0,2]
productOfNumbers.add(5)        # [3,0,2,5]
productOfNumbers.add(4)        # [3,0,2,5,4]
print(productOfNumbers.getProduct(3)) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(2)) # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(4)) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)        # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2)) # return 32. The product of the last 2 numbers is 4 * 8 = 32 
